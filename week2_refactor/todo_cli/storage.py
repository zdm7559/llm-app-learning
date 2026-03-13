import json
import os
import logging

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TASKS_FILE = os.path.join(BASE_DIR, "tasks.json")


def load_tasks():
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            tasks = json.load(f)
        logging.info("成功读取任务文件")
        return tasks
    except FileNotFoundError:
        logging.warning("任务文件不存在，已初始化为空列表")
        return []
    except json.JSONDecodeError:
        logging.error("任务文件 JSON 格式错误，已重置为空列表")
        print("任务文件格式错误，已重置为空列表。")
        return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)
    logging.info("任务已保存到 tasks.json")