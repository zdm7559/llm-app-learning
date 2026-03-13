import logging
from storage import save_tasks


def show_tasks(tasks):
    if tasks:
        logging.info("用户查看任务列表")
        print("当前任务列表：")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        logging.info("当前没有任务可显示")
        print("没有任务")


def add_task(tasks):
    task = input("请输入你的任务：").strip()
    if not task:
        logging.warning("用户输入了空任务内容")
        print("任务内容不能为空")
        return

    tasks.append(task)
    save_tasks(tasks)
    logging.info(f"成功添加任务: {task}")
    print("添加成功")


def delete_task(tasks):
    if not tasks:
        logging.warning("当前没有任务可以删除")
        print("当前没有任务可以删除")
        return

    show_tasks(tasks)
    try:
        index = int(input("请输入想要删除任务的编号：").strip())
        if 1 <= index <= len(tasks):
            removed_task = tasks.pop(index - 1)
            save_tasks(tasks)
            logging.info(f"成功删除任务: {removed_task}")
            print(f"已删除任务：{removed_task}")
        else:
            logging.warning(f"用户输入了超出范围的任务编号: {index}")
            print("没有此任务")
    except ValueError:
        logging.error("用户输入了非法的删除编号")
        print("请输入合法的数字编号")