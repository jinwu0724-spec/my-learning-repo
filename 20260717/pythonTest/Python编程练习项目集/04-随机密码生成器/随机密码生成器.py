# -*- coding: utf-8 -*-
"""
随机密码生成器

功能：
- 根据指定长度生成随机密码
- 可选是否包含大写字母、小写字母、数字和特殊符号
- 确保至少包含每种选中的字符类型
- 提供命令行入口
"""

import argparse
import random
import string


def generate_password(
    length: int = 12,
    use_upper: bool = True,
    use_lower: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True,
) -> str:
    """
    生成随机密码。

    :param length: 密码长度，必须大于等于选中的字符类型数
    :param use_upper: 是否包含大写字母
    :param use_lower: 是否包含小写字母
    :param use_digits: 是否包含数字
    :param use_symbols: 是否包含特殊符号
    :return: 生成的随机密码
    :raises ValueError: 参数非法
    """
    if length < 1:
        raise ValueError("密码长度必须大于等于 1。")

    categories = []
    if use_upper:
        categories.append(string.ascii_uppercase)
    if use_lower:
        categories.append(string.ascii_lowercase)
    if use_digits:
        categories.append(string.digits)
    if use_symbols:
        categories.append(string.punctuation)

    if not categories:
        raise ValueError("至少需要选择一种字符类型。")

    if length < len(categories):
        raise ValueError(
            f"密码长度至少为 {len(categories)} 以包含所有选中的字符类型。"
        )

    # 确保每种选中的字符类型至少出现一次
    password = [random.choice(category) for category in categories]

    # 剩余字符从所有候选字符中随机选择
    all_chars = "".join(categories)
    password.extend(random.choice(all_chars) for _ in range(length - len(categories)))

    random.shuffle(password)
    return "".join(password)


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description="随机密码生成器")
    parser.add_argument("-l", "--length", type=int, default=12, help="密码长度")
    parser.add_argument(
        "--no-upper", action="store_true", help="不包含大写字母"
    )
    parser.add_argument(
        "--no-lower", action="store_true", help="不包含小写字母"
    )
    parser.add_argument(
        "--no-digits", action="store_true", help="不包含数字"
    )
    parser.add_argument(
        "--no-symbols", action="store_true", help="不包含特殊符号"
    )

    args = parser.parse_args()
    password = generate_password(
        length=args.length,
        use_upper=not args.no_upper,
        use_lower=not args.no_lower,
        use_digits=not args.no_digits,
        use_symbols=not args.no_symbols,
    )
    print(f"生成的密码: {password}")


if __name__ == "__main__":
    main()