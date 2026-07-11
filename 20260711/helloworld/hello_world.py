"""创意 Hello World 展示脚本。

本脚本通过面向对象的方式和 ASCII 艺术，以打字机动态效果展示 "Hello World"，
避免简单直接的 print 输出。所有展示内容与时间参数均可配置，便于扩展。
"""

import random
import sys
import threading
import time
from dataclasses import dataclass


# =============================================================================
# 可配置常量（避免硬编码）
# =============================================================================

TARGET_TEXT: str = "Hello World"
"""要展示的核心文本内容。"""

TYPING_DELAY_MIN: float = 0.03
"""打字机效果的最小字符延迟（秒）。"""

TYPING_DELAY_MAX: float = 0.12
"""打字机效果的最大字符延迟（秒）。"""

RANDOM_SEED: int | None = None
"""随机种子，设为整数可复现打字节奏；None 表示每次随机。"""

PROGRESS_BAR_COUNT: int = 4
"""同时运行的进度条数量。"""

PROGRESS_BAR_WIDTH: int = 30
"""每个进度条的字符宽度。"""

PROGRESS_BAR_SPEEDS: tuple[float, ...] = (0.05, 0.08, 0.12, 0.15)
"""各进度条工作线程的更新间隔（秒），按索引循环使用。"""

PROGRESS_BAR_CHARS: tuple[str, ...] = ("#", "=", "*", "+")
"""各进度条的填充字符，按索引循环使用。"""

PROGRESS_REFRESH_INTERVAL: float = 0.05
"""ANSI 模式下渲染线程的刷新间隔（秒）。"""

ASCII_FONT: dict[str, list[str]] = {
    "H": [
        "H   H",
        "H   H",
        "HHHHH",
        "H   H",
        "H   H",
    ],
    "e": [
        " eee ",
        "e   e",
        "eeeee",
        "e    ",
        " eee ",
    ],
    "l": [
        "l    ",
        "l    ",
        "l    ",
        "l    ",
        "lllll",
    ],
    "o": [
        " ooo ",
        "o   o",
        "o   o",
        "o   o",
        " ooo ",
    ],
    " ": [
        "     ",
        "     ",
        "     ",
        "     ",
        "     ",
    ],
    "W": [
        "W   W",
        "W   W",
        "W W W",
        "WW WW",
        "W   W",
    ],
    "r": [
        "rrrr ",
        "r   r",
        "rrrr ",
        "r  r ",
        "r   r",
    ],
    "d": [
        "    d",
        "    d",
        " dddd",
        "d   d",
        " dddd",
    ],
}
"""简易 5x5 ASCII 字符画映射，键为字符，值为 5 行字符串列表。"""


# =============================================================================
# 数据类：渲染配置
# =============================================================================

@dataclass(frozen=True)
class RenderConfig:
    """控制文本展示行为的配置对象。

    Attributes:
        text: 要展示的目标字符串。
        delay_min: 打字机效果的最小字符延迟（秒）。
        delay_max: 打字机效果的最大字符延迟（秒）。
        reveal_prefix: 每次刷新行前输出的前缀字符。
        cursor: 模拟光标闪烁的字符。
        progress_bar_count: 同时运行的进度条数量。
        progress_bar_width: 每个进度条的字符宽度。
        progress_bar_speeds: 各进度条工作线程的更新间隔（秒）。
        progress_bar_chars: 各进度条的填充字符。
        progress_refresh_interval: ANSI 模式下渲染线程的刷新间隔（秒）。
        use_ansi: 是否使用 ANSI 转义码；None 表示自动检测。
    """

    text: str = TARGET_TEXT
    delay_min: float = TYPING_DELAY_MIN
    delay_max: float = TYPING_DELAY_MAX
    reveal_prefix: str = ">> "
    cursor: str = "_"
    progress_bar_count: int = PROGRESS_BAR_COUNT
    progress_bar_width: int = PROGRESS_BAR_WIDTH
    progress_bar_speeds: tuple[float, ...] = PROGRESS_BAR_SPEEDS
    progress_bar_chars: tuple[str, ...] = PROGRESS_BAR_CHARS
    progress_refresh_interval: float = PROGRESS_REFRESH_INTERVAL
    use_ansi: bool | None = None


# =============================================================================
# 进度条工作线程
# =============================================================================

class ProgressBarWorker(threading.Thread):
    """独立推进单条进度条的工作线程。

    每个实例负责一条进度条，按照配置的速度从 0 递增到 100，
    并将当前进度写入共享状态字典。控制台绘制统一由独立的渲染线程完成，
    工作线程不直接操作标准输出，从而避免多线程输出交错。

    Attributes:
        worker_id: 进度条编号，用于区分不同进度条。
        config: 渲染配置对象。
        state: 共享进度状态字典，键为 worker_id，值为 0~100 的整数。
        state_lock: 保护 ``state`` 读写的互斥锁。
        stop_event: 用于通知线程提前退出的事件。
    """

    def __init__(
        self,
        worker_id: int,
        config: RenderConfig,
        state: dict[int, int],
        state_lock: threading.Lock,
        stop_event: threading.Event,
    ) -> None:
        """初始化工作线程。

        Args:
            worker_id: 进度条编号。
            config: 渲染配置对象。
            state: 共享进度状态字典。
            state_lock: 状态锁。
            stop_event: 停止事件。
        """
        super().__init__(name=f"ProgressBar-{worker_id}", daemon=True)
        self.worker_id = worker_id
        self.config = config
        self.state = state
        self.state_lock = state_lock
        self.stop_event = stop_event
        self.speed = config.progress_bar_speeds[worker_id % len(config.progress_bar_speeds)]
        self.fill_char = config.progress_bar_chars[worker_id % len(config.progress_bar_chars)]
        self.total = 100

    def run(self) -> None:
        """线程主逻辑：按速度递增进度并更新共享状态。"""
        for value in range(self.total + 1):
            if self.stop_event.is_set():
                break

            with self.state_lock:
                self.state[self.worker_id] = value

            # 到达 100% 后无需再休眠
            if value < self.total:
                time.sleep(self.speed)


# =============================================================================
# 核心渲染器
# =============================================================================

class HelloWorldRenderer:
    """负责以创意方式渲染 "Hello World"。

    支持三种展示模式：
    1. typewriter: 逐字打印的打字机效果；
    2. ascii_art: 使用 ASCII 艺术字符画组合输出；
    3. progress_bars: 多线程字符进度条效果。

    所有模式均通过 ``render`` 方法统一调用，便于后续扩展新展示模式。
    """

    def __init__(self, config: RenderConfig | None = None) -> None:
        """初始化渲染器。

        Args:
            config: 渲染配置，若未提供则使用默认配置。
        """
        self.config = config or RenderConfig()

    # -------------------------------------------------------------------------
    # 公共 API
    # -------------------------------------------------------------------------

    def render(self, mode: str = "typewriter") -> None:
        """根据指定模式渲染 "Hello World"。

        Args:
            mode: 展示模式，可选 "typewriter"、"ascii_art" 或 "progress_bars"。

        Raises:
            ValueError: 当指定了未知的展示模式时抛出。
        """
        match mode:
            case "typewriter":
                self._render_typewriter()
            case "ascii_art":
                self._render_ascii_art()
            case "progress_bars":
                self._render_progress_bars()
            case _:
                raise ValueError(
                    f"未知的展示模式: {mode!r}，请选择 'typewriter'、'ascii_art' 或 'progress_bars'"
                )

    # -------------------------------------------------------------------------
    # 内部实现
    # -------------------------------------------------------------------------

    def _random_delay(self) -> float:
        """生成一个介于配置最小、最大延迟之间的随机停顿时间。"""
        return random.uniform(self.config.delay_min, self.config.delay_max)

    def _render_typewriter(self) -> None:
        """以打字机效果逐字输出目标文本。

        输出过程中会模拟光标闪烁，增强动态视觉体验。
        """
        prefix = self.config.reveal_prefix
        cursor = self.config.cursor
        text = self.config.text

        # 先输出空行和标题提示
        print("\n准备展示创意 Hello World ...\n")
        time.sleep(0.5)

        # 逐字输出并刷新同一行，模拟打字机效果
        for index, char in enumerate(text, start=1):
            visible = text[:index]
            sys.stdout.write(f"\r{prefix}{visible}{cursor}")
            sys.stdout.flush()
            time.sleep(self._random_delay())

        # 输出完成，定格最终文本并闪烁光标
        sys.stdout.write(f"\r{prefix}{text}  ")
        sys.stdout.flush()
        time.sleep(0.3)
        print(f"\n\n{'=' * 40}")
        print("展示完成！")
        print(f"{'=' * 40}\n")

    def _render_ascii_art(self) -> None:
        """使用 ASCII 艺术字符画组合输出目标文本。

        目标文本中的每个字符都会从 ``ASCII_FONT`` 中查找对应图案，
        横向拼接后逐行输出。若字符未定义，则以占位块显示，便于扩展。
        """
        text = self.config.text
        lines: list[list[str]] = [[] for _ in range(5)]

        for char in text:
            art = ASCII_FONT.get(char)
            if art is None:
                # 未定义字符使用占位块，保证输出不中断
                art = self._fallback_art(char)
            for row_index, row in enumerate(art):
                lines[row_index].append(row)

        print("\n" + " " * 12 + "ASCII 艺术版 Hello World")
        print("-" * 60)
        for row_parts in lines:
            print("  " + " ".join(row_parts))
        print("-" * 60 + "\n")

    # -------------------------------------------------------------------------
    # 多线程进度条实现
    # -------------------------------------------------------------------------

    def _supports_ansi(self) -> bool:
        """判断当前终端是否支持 ANSI 转义码。

        若配置中显式指定了 ``use_ansi``，则直接采用；否则结合 TTY 检测
        与 Windows 控制台能力进行判断。

        Returns:
            支持 ANSI 转义码返回 True，否则返回 False。
        """
        if self.config.use_ansi is not None:
            return self.config.use_ansi

        if not sys.stdout.isatty():
            return False

        # Windows 系统尝试启用虚拟终端处理；失败则退化为非 ANSI 模式
        if sys.platform == "win32":
            try:
                import ctypes

                kernel32 = ctypes.windll.kernel32
                handle = kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE
                mode = ctypes.c_uint32()
                if not kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
                    return False
                ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
                if not (mode.value & ENABLE_VIRTUAL_TERMINAL_PROCESSING):
                    new_mode = mode.value | ENABLE_VIRTUAL_TERMINAL_PROCESSING
                    if not kernel32.SetConsoleMode(handle, new_mode):
                        return False
            except (ImportError, AttributeError, OSError):
                return False

        return True

    def _render_progress_bars(self) -> None:
        """以多线程方式渲染多个字符进度条。

        每个进度条由独立的工作线程推进，渲染线程负责统一绘制。
        使用两把锁分别保护共享状态和控制台输出，避免线程间输出混乱。
        所有线程在正常完成或用户中断时均会被正确回收。
        """
        count = self.config.progress_bar_count
        state: dict[int, int] = {i: 0 for i in range(count)}
        state_lock = threading.Lock()
        console_lock = threading.Lock()
        stop_event = threading.Event()
        all_done = threading.Event()
        use_ansi = self._supports_ansi()

        workers = [
            ProgressBarWorker(
                worker_id=i,
                config=self.config,
                state=state,
                state_lock=state_lock,
                stop_event=stop_event,
            )
            for i in range(count)
        ]

        render_thread = threading.Thread(
            target=self._render_loop,
            args=(state, state_lock, console_lock, stop_event, all_done, workers, use_ansi),
            name="ProgressBarRenderer",
            daemon=True,
        )

        try:
            print("\n准备展示多线程字符进度条 ...\n")
            time.sleep(0.3)

            for worker in workers:
                worker.start()
            render_thread.start()

            # 等待所有工作线程自然结束
            for worker in workers:
                worker.join()

            # 通知渲染线程所有任务已完成，再绘制最后一帧
            all_done.set()
            render_thread.join(timeout=2.0)

            with console_lock:
                if not use_ansi:
                    sys.stdout.write("\n")
                sys.stdout.write("\n")
                sys.stdout.flush()

            print(f"{'=' * 40}")
            print("所有进度条已完成！")
            print(f"{'=' * 40}\n")
        except KeyboardInterrupt:
            stop_event.set()
        finally:
            stop_event.set()
            for worker in workers:
                worker.join(timeout=1.0)
            render_thread.join(timeout=1.0)
            sys.stdout.flush()

    def _render_loop(
        self,
        state: dict[int, int],
        state_lock: threading.Lock,
        console_lock: threading.Lock,
        stop_event: threading.Event,
        all_done: threading.Event,
        workers: list[ProgressBarWorker],
        use_ansi: bool,
    ) -> None:
        """渲染线程主循环：周期性读取状态并统一绘制所有进度条。

        Args:
            state: 共享进度状态字典。
            state_lock: 状态锁。
            console_lock: 控制台输出锁。
            stop_event: 停止事件。
            all_done: 所有工作线程完成事件。
            workers: 工作线程列表，用于获取每个进度条的填充字符。
            use_ansi: 是否使用 ANSI 转义码。
        """
        # 初始绘制空白进度条框架
        self._draw_progress_bars(state, console_lock, workers, use_ansi, first_draw=True)

        while not stop_event.is_set():
            self._draw_progress_bars(state, console_lock, workers, use_ansi, first_draw=False)

            if all_done.is_set():
                # 最后一帧：确保所有进度条都显示为 100%
                self._draw_progress_bars(state, console_lock, workers, use_ansi, first_draw=False)
                break

            time.sleep(self.config.progress_refresh_interval)

    def _draw_progress_bars(
        self,
        state: dict[int, int],
        console_lock: threading.Lock,
        workers: list[ProgressBarWorker],
        use_ansi: bool,
        first_draw: bool,
    ) -> None:
        """构造并输出所有进度条。

        Args:
            state: 共享进度状态字典。
            console_lock: 控制台输出锁。
            workers: 工作线程列表，用于获取每个进度条的填充字符。
            use_ansi: 是否使用 ANSI 转义码。
            first_draw: 是否为首次绘制。
        """
        count = self.config.progress_bar_count
        width = self.config.progress_bar_width

        with console_lock:
            if use_ansi:
                # 首次绘制不需要上移光标；后续绘制先回到进度条区域顶部
                if not first_draw:
                    sys.stdout.write(f"\033[{count}A")

                for worker in workers:
                    value = state.get(worker.worker_id, 0)
                    filled = int(value / 100 * width)
                    empty = width - filled
                    bar = worker.fill_char * filled + "-" * empty
                    line = f"[任务-{worker.worker_id + 1}] [{bar}] {value:3d}%"
                    sys.stdout.write(f"\033[2K\r{line}\n")
                sys.stdout.flush()
            else:
                # 非 ANSI 模式：将所有进度条合并为一行，用 \r 回到行首刷新
                parts = []
                for worker in workers:
                    value = state.get(worker.worker_id, 0)
                    filled = int(value / 100 * width)
                    empty = width - filled
                    bar = worker.fill_char * filled + "-" * empty
                    parts.append(f"[{worker.worker_id + 1}:{bar}] {value:3d}%")
                line = " | ".join(parts)
                sys.stdout.write(f"\r{line}")
                sys.stdout.flush()

    @staticmethod
    def _fallback_art(char: str) -> list[str]:
        """为未定义字符生成 5x5 占位图案。

        Args:
            char: 需要生成占位图案的单个字符。

        Returns:
            5 行字符串组成的占位图案列表。
        """
        return [
            "?????",
            "?   ?",
            f"? {char[:1]} ?",
            "?   ?",
            "?????",
        ]


# =============================================================================
# 程序入口
# =============================================================================

def main() -> None:
    """脚本入口函数。

    配置随机种子以保证可复现性（可选），随后依次展示打字机效果、
    ASCII 艺术效果以及多线程字符进度条效果。
    """
    if RANDOM_SEED is not None:
        random.seed(RANDOM_SEED)

    config = RenderConfig()
    renderer = HelloWorldRenderer(config)

    # 模式一：打字机动态效果
    renderer.render(mode="typewriter")

    # 模式二：ASCII 艺术静态效果
    renderer.render(mode="ascii_art")

    # 模式三：多线程字符进度条效果
    renderer.render(mode="progress_bars")


if __name__ == "__main__":
    main()
