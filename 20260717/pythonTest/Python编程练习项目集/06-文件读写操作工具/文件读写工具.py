# -*- coding: utf-8 -*-
"""
文件读写操作工具

功能：
- 读取文本文件内容
- 写入/覆盖文本文件
- 追加文本内容
- 复制文件
- 统计文件行数
- 在文件中搜索关键字
- 列示目录内容
"""

import argparse
import os
import shutil
from typing import List


def read_text_file(path: str, encoding: str = "utf-8") -> str:
    """读取指定文本文件的全部内容。"""
    with open(path, "r", encoding=encoding) as file:
        return file.read()


def write_text_file(path: str, content: str, encoding: str = "utf-8") -> None:
    """将内容写入文件，若文件已存在则覆盖。"""
    with open(path, "w", encoding=encoding) as file:
        file.write(content)


def append_text_file(path: str, content: str, encoding: str = "utf-8") -> None:
    """将内容追加到文件末尾。"""
    with open(path, "a", encoding=encoding) as file:
        file.write(content)


def copy_file(source: str, destination: str) -> None:
    """复制文件到目标路径。"""
    shutil.copy2(source, destination)


def count_lines(path: str, encoding: str = "utf-8") -> int:
    """统计文件行数。"""
    with open(path, "r", encoding=encoding) as file:
        return sum(1 for _ in file)


def search_text(path: str, keyword: str, encoding: str = "utf-8") -> List[int]:
    """
    在文件中搜索关键字，返回包含关键字的行号列表（从 1 开始）。
    """
    matched_lines = []
    with open(path, "r", encoding=encoding) as file:
        for line_number, line in enumerate(file, start=1):
            if keyword in line:
                matched_lines.append(line_number)
    return matched_lines


def list_directory(directory: str = ".") -> List[str]:
    """列示指定目录下的文件和文件夹名称。"""
    return sorted(os.listdir(directory))


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description="文件读写操作工具")
    subparsers = parser.add_subparsers(dest="command", required=True)

    read_parser = subparsers.add_parser("read", help="读取文件")
    read_parser.add_argument("path", help="文件路径")

    write_parser = subparsers.add_parser("write", help="写入文件")
    write_parser.add_argument("path", help="文件路径")
    write_parser.add_argument("content", help="写入内容")

    append_parser = subparsers.add_parser("append", help="追加内容")
    append_parser.add_argument("path", help="文件路径")
    append_parser.add_argument("content", help="追加内容")

    copy_parser = subparsers.add_parser("copy", help="复制文件")
    copy_parser.add_argument("source", help="源文件路径")
    copy_parser.add_argument("destination", help="目标文件路径")

    count_parser = subparsers.add_parser("count", help="统计行数")
    count_parser.add_argument("path", help="文件路径")

    search_parser = subparsers.add_parser("search", help="搜索关键字")
    search_parser.add_argument("path", help="文件路径")
    search_parser.add_argument("keyword", help="关键字")

    list_parser = subparsers.add_parser("list", help="列示目录")
    list_parser.add_argument("--dir", default=".", help="目录路径")

    args = parser.parse_args()

    if args.command == "read":
        print(read_text_file(args.path))
    elif args.command == "write":
        write_text_file(args.path, args.content)
        print(f"已写入: {args.path}")
    elif args.command == "append":
        append_text_file(args.path, args.content)
        print(f"已追加: {args.path}")
    elif args.command == "copy":
        copy_file(args.source, args.destination)
        print(f"已复制: {args.source} -> {args.destination}")
    elif args.command == "count":
        print(f"行数: {count_lines(args.path)}")
    elif args.command == "search":
        lines = search_text(args.path, args.keyword)
        print(f"匹配行号: {lines}")
    elif args.command == "list":
        for name in list_directory(args.dir):
            print(name)


if __name__ == "__main__":
    main()