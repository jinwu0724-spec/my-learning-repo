# -*- coding: utf-8 -*-
"""
简易通讯录管理系统

功能：
- 添加、删除、修改联系人
- 按姓名或关键字搜索联系人
- 将联系人数据持久化到 JSON 文件
- 提供命令行交互界面
"""

import argparse
import json
import os
from typing import Dict, List, Optional


class Contact:
    """联系人数据类。"""

    def __init__(self, name: str, phone: str, email: str):
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self) -> dict:
        return {
            "姓名": self.name,
            "电话": self.phone,
            "邮箱": self.email,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Contact":
        return cls(data["姓名"], data["电话"], data["邮箱"])

    def __repr__(self) -> str:
        return f"Contact(name={self.name}, phone={self.phone}, email={self.email})"


class ContactManager:
    """通讯录管理器，负责联系人的增删改查与持久化。"""

    def __init__(self, data_file: str = "通讯录数据.json"):
        self.data_file = data_file
        self.contacts: Dict[str, Contact] = {}
        self.load()

    def load(self) -> None:
        """从 JSON 文件加载联系人数据。"""
        if not os.path.exists(self.data_file):
            self.contacts = {}
            return

        with open(self.data_file, "r", encoding="utf-8") as file:
            data = json.load(file)

        self.contacts = {
            item["姓名"]: Contact.from_dict(item) for item in data
        }

    def save(self) -> None:
        """将联系人数据保存到 JSON 文件。"""
        data = [contact.to_dict() for contact in self.contacts.values()]
        with open(self.data_file, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

    def add(self, name: str, phone: str, email: str) -> None:
        """添加联系人。"""
        if name in self.contacts:
            raise ValueError(f"联系人 '{name}' 已存在。")
        self.contacts[name] = Contact(name, phone, email)
        self.save()

    def delete(self, name: str) -> None:
        """删除联系人。"""
        if name not in self.contacts:
            raise ValueError(f"联系人 '{name}' 不存在。")
        del self.contacts[name]
        self.save()

    def update(
        self, name: str, phone: Optional[str] = None, email: Optional[str] = None
    ) -> None:
        """更新联系人信息。"""
        if name not in self.contacts:
            raise ValueError(f"联系人 '{name}' 不存在。")
        if phone is not None:
            self.contacts[name].phone = phone
        if email is not None:
            self.contacts[name].email = email
        self.save()

    def search(self, keyword: str) -> List[Contact]:
        """按关键字搜索联系人（支持姓名、电话、邮箱）。"""
        keyword = keyword.lower()
        return [
            contact
            for contact in self.contacts.values()
            if keyword in contact.name.lower()
            or keyword in contact.phone
            or keyword in contact.email.lower()
        ]

    def list_all(self) -> List[Contact]:
        """返回所有联系人。"""
        return list(self.contacts.values())


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description="简易通讯录管理系统")
    parser.add_argument(
        "--file", default="通讯录数据.json", help="数据文件路径"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="添加联系人")
    add_parser.add_argument("name", help="姓名")
    add_parser.add_argument("phone", help="电话")
    add_parser.add_argument("email", help="邮箱")

    delete_parser = subparsers.add_parser("delete", help="删除联系人")
    delete_parser.add_argument("name", help="姓名")

    update_parser = subparsers.add_parser("update", help="更新联系人")
    update_parser.add_argument("name", help="姓名")
    update_parser.add_argument("--phone", help="新电话")
    update_parser.add_argument("--email", help="新邮箱")

    search_parser = subparsers.add_parser("search", help="搜索联系人")
    search_parser.add_argument("keyword", help="关键字")

    list_parser = subparsers.add_parser("list", help="列示所有联系人")

    args = parser.parse_args()
    manager = ContactManager(args.file)

    if args.command == "add":
        manager.add(args.name, args.phone, args.email)
        print(f"已添加联系人: {args.name}")
    elif args.command == "delete":
        manager.delete(args.name)
        print(f"已删除联系人: {args.name}")
    elif args.command == "update":
        manager.update(args.name, args.phone, args.email)
        print(f"已更新联系人: {args.name}")
    elif args.command == "search":
        results = manager.search(args.keyword)
        if not results:
            print("未找到匹配的联系人。")
        for contact in results:
            print(f"{contact.name} | {contact.phone} | {contact.email}")
    elif args.command == "list":
        contacts = manager.list_all()
        if not contacts:
            print("通讯录为空。")
        for contact in contacts:
            print(f"{contact.name} | {contact.phone} | {contact.email}")


if __name__ == "__main__":
    main()