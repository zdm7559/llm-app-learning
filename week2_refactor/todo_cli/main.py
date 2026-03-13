import logging
from logger_config import setup_logger
from storage import load_tasks
from task_manager import show_tasks, add_task, delete_task


def show_menu():
    print("\n==== 待办事项管理器 ====")
    print("1. 查看任务")
    print("2. 添加任务")
    print("3. 删除任务")
    print("0. 退出")


def main():
    setup_logger()
    logging.info("待办事项管理器启动")

    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("请输入你的选择：").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "0":
            logging.info("程序退出")
            print("程序已退出。")
            break
        else:
            logging.warning(f"用户输入了无效菜单选项: {choice}")
            print("输入无效，请重新选择。")


if __name__ == "__main__":
    main()