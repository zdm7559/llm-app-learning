import json
from typing import List, Dict

STUDENTS_FILE = "students.json"  # 存储学生数据的 JSON 文件

def load_students() -> List[Dict]:
    """从 students.json 中加载学生数据"""
    try:
        with open(STUDENTS_FILE, "r", encoding="utf-8") as f:
            students = json.load(f)
        return students
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # 文件不存在或格式错误时返回空列表

def save_students(students: List[Dict]):
    """把学生数据写入 students.json 文件"""
    with open(STUDENTS_FILE, "w", encoding="utf-8") as f:
        json.dump(students, f, ensure_ascii=False, indent=4)