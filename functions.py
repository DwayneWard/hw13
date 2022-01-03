import json


def read_json(file) -> list:
    """Функция реализует чтение данных об уже размещенных постах
    Аргументов функции передается .json файл, который нужно прочитать"""
    with open(file, encoding="utf-8") as f:
        json_data = json.load(f)
    return json_data


def tags(json_data) -> set:
    """Функция возвращает список тэгов, из текста всех постов, размещенных на сайте.
    Аргументом функции передаются прочитанные из файла .json данные"""
    match = []

    for post in json_data:
        text = post["content"].split(" ")
        for word in text:
            if "#" in word:
                tag = word.replace("#", "")
                tag = tag.replace("!", "")
                match.append(tag)
    # Приведение к множеству, для исключения повторения тэгов в списке.
    match = set(match)

    return match


def tag_search(json_data, tag) -> list:
    """Функция возвращает список постов, в которых находится тэг, введенный пользователем.
    Аргументами функции передаются:
    1) Прочитанные из файла .json данные,
    2) тэг, введенный пользователем"""
    hash_tag = "#" + tag
    taged_posts = []
    for post in json_data:
        if hash_tag in post["content"]:
            taged_posts.append(post)

    return taged_posts


def write_json(file, json_data):
    """Функция реализует запись данных в файл .json.
    Аргументами функции передаются:
    1) Файл, куда необходимо записать данные,
    2) Данные, которые необходимо записать"""
    with open(file, "w") as f:
        json.dump(json_data, f, ensure_ascii=False)
