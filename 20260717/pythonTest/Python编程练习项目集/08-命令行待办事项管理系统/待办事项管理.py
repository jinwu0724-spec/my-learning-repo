# -*- coding: utf-8 -*-
"""
命令行待办事项管理系统

功能：
- 添加待办事项
- 标记事项为已完成
- 删除待办事项
- 列示所有事项，可按状态筛选
- 数据持久化到 JSON 文件
"""

import argparse
import datetime
import json
import os
from typing import Dict, List, Optional


class TodoItem:
    """待办事项数据类。"""

    def __init__(
        self,
        task_id: int,
        title: str,
        status: str = "待完成",
        created_at: Optional[str] = None,
    ):
        self.task_id = task_id
        self.title = title
        self.status = status
        self.created_at = created_at or datetime.datetime.now().isoformat()

    def to_dict(self) -> dict:
        return {
            "id": self.task_id,
            "title": self.title,
            "status": self.status,
            "created_at": self.created_at,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "TodoItem":
        return cls(
            task_id=data["id"],
            title=data["title"],
            status=data["status"],
            created_at=data.get("created_at"),
        )


class TodoManager:
    """待办事项管理器。"""

    def __init__(self, data_file: str = "待办数据.json"):
        self.data_file = data_file
        self.tasks: Dict[int, TodoItem] = {}
        self.next_id = 1
        self.load()

    def load(self) -> None:
        """从 JSON 文件加载待办事项。"""
        if not os.path.exists(self.data_file):
            self.tasks = {}
            self.next_id = 1
            return

        with open(self.data_file, "r", encoding="utf-8") as file:
            data = json.load(file)

        self.tasks = {item["id"]: TodoItem.from_dict(item) for item in data}
        self.next_id = max(self.tasks.keys(), default=0) + 1

    def save(self) -> None:
        """保存待办事项到 JSON 文件。"""
        data = [task.to_dict() for task in self.tasks.values()]
        with open(self.data_file, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

    def add(self, title: str) -> int:
        """添加新的待办事项。"""
        task_id = self.next_id
        self.tasks[task_id] = TodoItem(task_id, title)
        self.next_id += 1
        self.save()
        return task_id

    def complete(self, task_id: int) -> None:
        """将事项标记为已完成。"""
        if task_id not in self.tasks:
            raise ValueError(f"待办事项 {task_id} 不存在。")
        self.tasks[task_id].status = "已完成"
        self.save()

    def remove(self, task_id: int) -> None:
        """删除待办事项。"""
        if task_id not in self.tasks:
            raise ValueError(f"待办事项 {task_id} 不存在。")
        del self.tasks[task_id]
        self.save()

    def list(self, status: Optional[str] = None) -> List[TodoItem]:
        """列示待办事项，可按状态筛选。"""
        tasks = list(self.tasks.values())
        if status:
            tasks = [task for task in tasks if task.status == status]
        return sorted(tasks, key=lambda task: task.task_id)

    def clear(self) -> None:
        """清空所有待办事项。"""
        self.tasks.clear()
        self.next_id = 1
        self.save()


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description="命令行待办事项管理系统")
    parser.add_argument("--file", default="待办数据.json", help="数据文件路径")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="添加待办事项")
    add_parser.add_argument("title", help="事项标题")

    complete_parser = subparsers.add_parser("complete", help="完成待办事项")
    complete_parser.add_argument("id", type=int, help="事项编号")

    remove_parser = subparsers.add_parser("remove", help="删除待办事项")
    remove_parser.add_argument("id", type=int, help="事项编号")

    list_parser = subparsers.add_parser("list", help="列示待办事项")
    list_parser.add_argument(
        "--status", choices=["待完成", "已完成"], help="按状态筛选"
    )

    clear_parser = subparsers.add_parser("clear", help="清空所有事项")

    args = parser.parse_args()
    manager = TodoManager(args.file)

    if args.command == "add":
        task_id = manager.add(args.title)
        print(f"已添加待办事项，编号: {task_id}")
    elif args.command == "complete":
        manager.complete(args.id)
        print(f"待办事项 {args.id} 已标记为已完成。")
    elif args.command == "remove":
        manager.remove(args.id)
        print(f"待办事项 {args.id} 已删除。")
    elif args.command == "list":
        tasks = manager.list(args.status)
        if not tasks:
            print("暂无待办事项。")
        for task in tasks:
            print(f"[{task.task_id}] {task.status} | {task.title} | {task.created_at}")
    elif args.command == "clear":
        manager.clear()
        print("已清空所有待办事项。")


if __name__ == "__main__":
    main()