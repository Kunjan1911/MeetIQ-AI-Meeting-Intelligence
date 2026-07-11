import os


def save_text(text, path):

    with open(path, "w", encoding="utf-8") as file:

        file.write(text)


def read_text(path):

    with open(path, "r", encoding="utf-8") as file:

        return file.read()