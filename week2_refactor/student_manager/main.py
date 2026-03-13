import logging
from logger_config import setup_logger
from operations import (
    add_student,
    show_all_students,
    query_student,
    update_student,
    delete_student
)

students = {}


def show_menu():
    print("\n==== 学生成绩管理系统 ====")
    print("1. 添加学生成绩")
    print("2. 查看所有学生成绩")
    print("3. 查询单个学生成绩")
    print("4. 修改学生成绩")
    print("5. 删除学生成绩")
    print("0. 退出")


def main():
    setup_logger()
    logging.info("学生成绩管理系统启动")

    while True:
        show_menu()
        choice = input("请输入你的选择: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            show_all_students(students)
        elif choice == "3":
            query_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "0":
            logging.info("学生成绩管理系统退出")
            print("程序已退出。")
            break
        else:
            logging.warning(f"用户输入了无效菜单选项: {choice}")
            print("输入无效，请重新选择。")


if __name__ == "__main__":
    main()