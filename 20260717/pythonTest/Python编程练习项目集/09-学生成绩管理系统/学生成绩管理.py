# -*- coding: utf-8 -*-
"""
学生成绩管理系统

功能：
- 添加、删除学生
- 为学生录入各科成绩
- 计算学生平均分
- 按平均分生成排名
- 将数据持久化到 JSON，支持导出 CSV
"""

import argparse
import csv
import json
import os
import statistics
from typing import Dict, List, Optional


class Student:
    """学生数据类。"""

    def __init__(self, student_id: str, name: str, scores: Optional[Dict[str, float]] = None):
        self.student_id = student_id
        self.name = name
        self.scores = scores or {}

    def to_dict(self) -> dict:
        return {
            "学号": self.student_id,
            "姓名": self.name,
            "成绩": self.scores,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Student":
        return cls(
            student_id=data["学号"],
            name=data["姓名"],
            scores=data.get("成绩", {}),
        )

    def average(self) -> Optional[float]:
        """返回平均分，无成绩时返回 None。"""
        if not self.scores:
            return None
        return statistics.mean(self.scores.values())


class StudentGradeManager:
    """学生成绩管理器。"""

    def __init__(self, data_file: str = "成绩数据.json"):
        self.data_file = data_file
        self.students: Dict[str, Student] = {}
        self.load()

    def load(self) -> None:
        """从 JSON 文件加载学生数据。"""
        if not os.path.exists(self.data_file):
            self.students = {}
            return

        with open(self.data_file, "r", encoding="utf-8") as file:
            data = json.load(file)

        self.students = {
            item["学号"]: Student.from_dict(item) for item in data
        }

    def save(self) -> None:
        """保存学生数据到 JSON 文件。"""
        data = [student.to_dict() for student in self.students.values()]
        with open(self.data_file, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

    def add_student(self, student_id: str, name: str) -> None:
        """添加学生。"""
        if student_id in self.students:
            raise ValueError(f"学号 {student_id} 已存在。")
        self.students[student_id] = Student(student_id, name)
        self.save()

    def remove_student(self, student_id: str) -> None:
        """删除学生。"""
        if student_id not in self.students:
            raise ValueError(f"学号 {student_id} 不存在。")
        del self.students[student_id]
        self.save()

    def add_score(self, student_id: str, subject: str, score: float) -> None:
        """为学生录入单科成绩。"""
        if student_id not in self.students:
            raise ValueError(f"学号 {student_id} 不存在。")
        if not 0 <= score <= 100:
            raise ValueError("成绩必须在 0 到 100 之间。")
        self.students[student_id].scores[subject] = score
        self.save()

    def get_average(self, student_id: str) -> Optional[float]:
        """获取指定学生的平均分。"""
        if student_id not in self.students:
            raise ValueError(f"学号 {student_id} 不存在。")
        return self.students[student_id].average()

    def get_ranking(self) -> List[Student]:
        """按平均分降序返回学生排名，无成绩者排在末尾。"""
        return sorted(
            self.students.values(),
            key=lambda s: s.average() if s.average() is not None else -1,
            reverse=True,
        )

    def export_csv(self, path: str) -> None:
        """将学生成绩导出为 CSV 文件。"""
        with open(path, "w", encoding="utf-8-sig", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["学号", "姓名", "科目", "成绩"])
            for student in self.students.values():
                for subject, score in student.scores.items():
                    writer.writerow([student.student_id, student.name, subject, score])


def main() -> None:
    """命令行入口。"""
    parser = argparse.ArgumentParser(description="学生成绩管理系统")
    parser.add_argument("--file", default="成绩数据.json", help="数据文件路径")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="添加学生")
    add_parser.add_argument("student_id", help="学号")
    add_parser.add_argument("name", help="姓名")

    score_parser = subparsers.add_parser("score", help="录入成绩")
    score_parser.add_argument("student_id", help="学号")
    score_parser.add_argument("subject", help="科目")
    score_parser.add_argument("score", type=float, help="成绩")

    avg_parser = subparsers.add_parser("average", help="查看平均分")
    avg_parser.add_argument("student_id", help="学号")

    rank_parser = subparsers.add_parser("rank", help="查看排名")

    export_parser = subparsers.add_parser("export", help="导出 CSV")
    export_parser.add_argument("path", help="CSV 文件路径")

    args = parser.parse_args()
    manager = StudentGradeManager(args.file)

    if args.command == "add":
        manager.add_student(args.student_id, args.name)
        print(f"已添加学生: {args.name}")
    elif args.command == "score":
        manager.add_score(args.student_id, args.subject, args.score)
        print("成绩已录入。")
    elif args.command == "average":
        average = manager.get_average(args.student_id)
        if average is None:
            print("该学生暂无成绩。")
        else:
            print(f"平均分: {average:.2f}")
    elif args.command == "rank":
        for index, student in enumerate(manager.get_ranking(), start=1):
            avg = student.average()
            avg_str = f"{avg:.2f}" if avg is not None else "无成绩"
            print(f"{index}. {student.name} ({student.student_id}) - {avg_str}")
    elif args.command == "export":
        manager.export_csv(args.path)
        print(f"已导出到: {args.path}")


if __name__ == "__main__":
    main()