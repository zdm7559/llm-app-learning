using = None  # 这一行可以删掉，不影响运行

students = {}


def show_menu():
    print("\n==== 学生成绩管理系统 ====")
    print("1. 添加学生成绩")
    print("2. 查看所有学生成绩")
    print("3. 查询单个学生成绩")
    print("4. 修改学生成绩")
    print("5. 删除学生成绩")
    print("0. 退出")


def add_student():
    name = input("请输入学生姓名: ").strip()
    if name in students:
        print("该学生已存在。")
        return

    try:
        score = float(input("请输入学生成绩: "))
        students[name] = score
        print("添加成功。")
    except ValueError:
        print("成绩输入无效，请输入数字。")


def show_all_students():
    if not students:
        print("当前没有学生信息。")
        return

    print("\n所有学生成绩如下：")
    for name, score in students.items():
        print(f"姓名: {name}, 成绩: {score}")


def query_student():
    name = input("请输入要查询的学生姓名: ").strip()
    if name in students:
        print(f"{name} 的成绩是: {students[name]}")
    else:
        print("未找到该学生。")


def update_student():
    name = input("请输入要修改成绩的学生姓名: ").strip()
    if name not in students:
        print("未找到该学生。")
        return

    try:
        new_score = float(input("请输入新的成绩: "))
        students[name] = new_score
        print("修改成功。")
    except ValueError:
        print("成绩输入无效，请输入数字。")


def delete_student():
    name = input("请输入要删除的学生姓名: ").strip()
    if name in students:
        del students[name]
        print("删除成功。")
    else:
        print("未找到该学生。")


def main():
    while True:
        show_menu()
        choice = input("请输入你的选择: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            show_all_students()
        elif choice == "3":
            query_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "0":
            print("程序已退出。")
            break
        else:
            print("输入无效，请重新选择。")


if __name__ == "__main__":
    main()