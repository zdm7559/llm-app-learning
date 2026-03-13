# operators.py主要负责增删改查具体逻辑

import logging


def add_student(students):
    name = input("请输入学生姓名: ").strip()
    if not name:
        logging.warning("用户输入了空姓名")
        print("学生姓名不能为空。")
        return

    if name in students:
        logging.warning(f"尝试添加已存在的学生: {name}")
        print("该学生已存在。")
        return

    try:
        score = float(input("请输入学生成绩: ").strip())
        students[name] = score
        logging.info(f"成功添加学生 {name}，成绩为 {score}")
        print("添加成功。")
    except ValueError:
        logging.error(f"学生 {name} 的成绩输入无效")
        print("成绩输入无效，请输入数字。")


def show_all_students(students):
    if not students:
        logging.info("当前没有学生信息可展示")
        print("当前没有学生信息。")
        return

    logging.info("开始展示所有学生成绩")
    print("\n所有学生成绩如下：")
    for name, score in students.items():
        print(f"姓名: {name}, 成绩: {score}")


def query_student(students):
    name = input("请输入要查询的学生姓名: ").strip()
    if name in students:
        logging.info(f"查询学生成功: {name}")
        print(f"{name} 的成绩是: {students[name]}")
    else:
        logging.warning(f"查询失败，学生不存在: {name}")
        print("未找到该学生。")


def update_student(students):
    name = input("请输入要修改成绩的学生姓名: ").strip()
    if name not in students:
        logging.warning(f"修改失败，学生不存在: {name}")
        print("未找到该学生。")
        return

    try:
        new_score = float(input("请输入新的成绩: ").strip())
        old_score = students[name]
        students[name] = new_score
        logging.info(f"修改学生 {name} 的成绩：{old_score} -> {new_score}")
        print("修改成功。")
    except ValueError:
        logging.error(f"修改学生 {name} 成绩时输入了非法值")
        print("成绩输入无效，请输入数字。")


def delete_student(students):
    name = input("请输入要删除的学生姓名: ").strip()
    if name in students:
        del students[name]
        logging.info(f"删除学生成功: {name}")
        print("删除成功。")
    else:
        logging.warning(f"删除失败，学生不存在: {name}")
        print("未找到该学生。")