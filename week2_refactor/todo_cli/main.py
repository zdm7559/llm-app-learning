tasks = []

def show_menu():
    print("\n==== 待办事项管理器 ====")
    print("1. 查看任务")
    print("2. 添加任务")
    print("3. 删除任务")
    print("0. 退出")

def show_tasks():
    if tasks:
        print("当前任务列表。")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}, {task}")
    else:
        print("没有任务")
def add_task():
    task = input("请输入你的任务：").strip()
    if not task:
        print("任务内容不能为空")
        return
    tasks.append(task)
    print("添加成功")

def delete_task():
    if not tasks:
        print("当前没有任务可以删除")
        return
    show_menu()
    try:
        index = int(input("请输入想要删除任务的编号：").strip())
        if 1 <= index <= len(tasks):
            removed_task = tasks.pop(index-1)
            print(f"已删除任务：{removed_task}")
        else:
            print("没有此任务")
    except ValueError:
        print("请输入合法的数字编号")

def main():
    while 1:
        show_menu()
        choice = input("请输入你的选择：").strip()

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "0":
            print("程序已退出。")
            break
        else:
            print("输入无效，请重新选择。")


if __name__ == "__main__":
    main()