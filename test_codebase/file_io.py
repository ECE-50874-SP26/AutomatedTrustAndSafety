import os


def read_file(path):
    if not os.path.exists(path):
        raise FileNotFoundError("File not found")

    with open(path, "r") as f:
        return f.read()


def write_file(path, content):
    with open(path, "w") as f:
        f.write(content)


def append_file(path, content):
    with open(path, "a") as f:
        f.write(content)


def list_files(directory):
    return os.listdir(directory)