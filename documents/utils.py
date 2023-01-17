import json


def read_text_file(file_path: str) -> str:
    with open(file_path, "r") as f:
        return f.read()


def write_text_file(file_path: str, text: str):
    with open(file_path, "w") as f:
        f.write(text)


def read_json(file_path: str) -> dict:
    with open(file_path, "r") as f:
        return json.load(f)


def save_json(file_path: str, data: dict):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
