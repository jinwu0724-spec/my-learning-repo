# -*- coding: utf-8 -*-
"""
简易日志分析工具

功能：
- 解析统一格式的日志条目
- 按日志级别统计数量
- 按关键字搜索日志
- 按时间范围过滤日志
"""

import argparse
import datetime
import re
from collections import Counter
from typing import List, Optional


# 日志格式示例: [2024-05-20 08:30:00] [INFO] 系统启动成功
LOG_PATTERN = re.compile(
    r"^\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] \[(\w+)\] (.*)$"
)


def parse_line(line: str) -> Optional[dict]:
    """
    解析单行日志。

    :return: 包含时间、级别、消息的字典；格式不匹配返回 None
    """
    match = LOG_PATTERN.match(line.strip())
    if not match:
        return None

    timestamp_str, level, message = match.groups()
    try:
        timestamp = datetime.datetime.strptime(
            timestamp_str, "%Y-%m-%d %H:%M:%S"
        )
    except ValueError:
        return None

    return {
        "timestamp": timestamp,
        "level": level,
        "message": message,
        "raw": line.strip(),
    }


def parse_log(text: str) -> List[dict]:
    """解析多行日志文本。"""
    entries = []
    for line in text.splitlines():
        entry = parse_line(line)
        if entry:
            entries.append(entry)
    return entries


def count_levels(entries: List[dict]) -> Counter:
    """统计各级别日志出现的次数。"""
    return Counter(entry["level"] for entry in entries)


def search_keyword(entries: List[dict], keyword: str) -> List[dict]:
    """在日志消息中搜索关键字。"""
    return [entry for entry in entries if keyword in entry["message"]]


def filter_by_time(
    entries: List[dict],
    start: datetime.datetime,
    end: datetime.datetime,
) -> List[dict]:
    """按时间范围过滤日志。"""
    return [
        entry for entry in entries if start <= entry["timestamp"] <= end
    ]


def read_log_file(path: str, encoding: str = "utf-8") -> str:
    """读取日志文件内容。"""
    with open(path, "r", encoding=encoding) as file:
        return file.read()


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description="简易日志分析工具")
    subparsers = parser.add_subparsers(dest="command", required=True)

    count_parser = subparsers.add_parser("count", help="统计各级别数量")
    count_parser.add_argument("path", help="日志文件路径")

    search_parser = subparsers.add_parser("search", help="搜索关键字")
    search_parser.add_argument("path", help="日志文件路径")
    search_parser.add_argument("keyword", help="关键字")

    filter_parser = subparsers.add_parser("filter", help="按时间范围过滤")
    filter_parser.add_argument("path", help="日志文件路径")
    filter_parser.add_argument("start", help="开始时间，格式 YYYY-MM-DD HH:MM:SS")
    filter_parser.add_argument("end", help="结束时间，格式 YYYY-MM-DD HH:MM:SS")

    args = parser.parse_args()
    text = read_log_file(args.path)
    entries = parse_log(text)

    if args.command == "count":
        levels = count_levels(entries)
        for level, count in sorted(levels.items()):
            print(f"{level}: {count}")
    elif args.command == "search":
        results = search_keyword(entries, args.keyword)
        for entry in results:
            print(entry["raw"])
    elif args.command == "filter":
        start = datetime.datetime.strptime(args.start, "%Y-%m-%d %H:%M:%S")
        end = datetime.datetime.strptime(args.end, "%Y-%m-%d %H:%M:%S")
        results = filter_by_time(entries, start, end)
        for entry in results:
            print(entry["raw"])


if __name__ == "__main__":
    main()