contacts = {}


def show_menu():
    print("\n==== 简单通讯录 ====")
    print("1. 添加联系人")
    print("2. 查看所有联系人")
    print("3. 查询联系人")
    print("4. 修改联系人")
    print("5. 删除联系人")
    print("0. 退出")


def add_contact():
    name = input("请输入联系人姓名: ").strip()
    if name in contacts:
        print("该联系人已存在。")
        return

    phone = input("请输入电话号码: ").strip()
    contacts[name] = phone
    print("添加成功。")


def show_all_contacts():
    if not contacts:
        print("通讯录为空。")
        return

    print("\n所有联系人如下：")
    for name, phone in contacts.items():
        print(f"姓名: {name}, 电话: {phone}")


def query_contact():
    name = input("请输入要查询的联系人姓名: ").strip()
    if name in contacts:
        print(f"{name} 的电话是: {contacts[name]}")
    else:
        print("未找到该联系人。")


def update_contact():
    name = input("请输入要修改的联系人姓名: ").strip()
    if name not in contacts:
        print("未找到该联系人。")
        return

    new_phone = input("请输入新的电话号码: ").strip()
    contacts[name] = new_phone
    print("修改成功。")


def delete_contact():
    name = input("请输入要删除的联系人姓名: ").strip()
    if name in contacts:
        del contacts[name]
        print("删除成功。")
    else:
        print("未找到该联系人。")


def main():
    while True:
        show_menu()
        choice = input("请输入你的选择: ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            show_all_contacts()
        elif choice == "3":
            query_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "0":
            print("程序已退出。")
            break
        else:
            print("输入无效，请重新选择。")


if __name__ == "__main__":
    main()