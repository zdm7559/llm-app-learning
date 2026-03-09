def count_words(filename):
    word_count = {}

    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read().lower()

            for ch in ",.!?;:()[]{}\"'":
                text = text.replace(ch, "")

            words = text.split()

            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

        return word_count

    except FileNotFoundError:
        print("文件不存在，请检查文件名。")
        return None


def main():
    filename = input("请输入要统计的文本文件名: ").strip()
    result = count_words(filename)

    if result is not None:
        print("\n词频统计结果：")
        for word, count in sorted(result.items(), key=lambda x: x[1], reverse=True):
            print(f"{word}: {count}")


if __name__ == "__main__":
    main()