import os


def read_file(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def list_text_files(data_dir: str) -> list[str]:
    files = []
    for name in os.listdir(data_dir):
        if name.endswith(".txt") or name.endswith(".md"):
            files.append(os.path.join(data_dir, name))
    return files