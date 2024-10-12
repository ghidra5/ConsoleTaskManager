# Программа должна поддерживать следующие функции:
# Добавление задачи: Пользователь может добавить новую задачу с указанием названия и описания.
# Просмотр всех задач: Пользователь может увидеть список всех задач.
# Удаление задачи: Пользователь может удалить задачу по её индексу или названию.
# Изменение статуса задачи: Пользователь может пометить задачу как выполненную или вернуть её в статус "не выполнена".
# Поиск задач: Пользователь может искать задачи по ключевым словам в названии или описании.
# Сохранение задач в файл: Список задач сохраняется в файл при выходе из программы, и загружается при следующем запуске.

import json
tasks = []


def add_task():
    error = False
    title = input("Введите название: ")
    description = input("Введите описание: ")
    for i, task in enumerate(tasks):
        if title in task['Название']:
            print("Введите уникальное название!")
            error = True
        elif len(title) == 0 or len(description) == 0:
            print("Введите корректное имя!")
            error = True
    if not error:
        task = {"Название": title, "Описание": description, "Завершено": False}
        tasks.append(task)
        print("Задача создана!")


def view_tasks():
    found = False
    for i, task in enumerate(tasks):
        print("#" + str(i) + " Название: " + task["Название"] + "\nОписание: " + task["Описание"] +
              "\nСтатус:", task["Завершено"], "\n")
        if not found:
            found = True
    if not found:
        print("Нет ни одной созданной задачи")


def del_task():
    found = False
    value = input("Введите индекс или имя задачи: ")
    try:
        index = int(value)
        if 0 <= index < len(tasks):
            deleted_task = tasks.pop(index)
            print(f"Задача '{deleted_task['Название']}' успешно удалена")
            found = True
    except ValueError:
        for i, task in enumerate(tasks):
            if task["Название"] == value:
                deleted_task = tasks.pop(i)
                print(f"Задача '{deleted_task['Название']}' успешно удалена")
                found = True
    if not found:
        print(f"Задача с индексом или именем '{value}' не найдена")


def edit_task():
    value = input("Введите индекс или название задачи, статус которой вы хотите изменить: ")
    try:
        index = int(value)
        switched = False
        if 0 <= index < len(tasks):
            for i, task in enumerate(tasks):
                if i == index:
                    selected_task = task
                    if selected_task["Завершено"]:
                        selected_task["Завершено"] = False
                        print(f"Статус задачи '{selected_task["Название"]}' был успешно изменен")
                        switched = True
                    elif not selected_task["Завершено"]:
                        selected_task["Завершено"] = True
                        print(f"Статус задачи '{selected_task["Название"]}' был успешно изменен")
                        switched = True
    except ValueError:
        switched = False
        for i, task in enumerate(tasks):
            if task["Название"] == value:
                selected_task = task
                if selected_task["Завершено"]:
                    selected_task["Завершено"] = False
                    print(f"Статус задачи '{selected_task["Название"]}' был успешно изменен")
                    switched = True
                elif not selected_task["Завершено"]:
                    selected_task["Завершено"] = True
                    print(f"Статус задачи '{selected_task["Название"]}' был успешно изменен")
                    switched = True
    if not switched:
        print(f"Задача с именем/индексом '{value}' не найдена")


def search_tasks():
    searched_task = input("Введите ключевое слово для поиска задачи по названию или описанию:\n").lower()
    found = False

    for task in tasks:
        title = task["Название"]
        description = task["Описание"].lower()
        if searched_task in title.lower() or searched_task in description.lower():
            print(f"Возможно, вы искали это:\n'{task["Название"]} {task["Описание"]}'")
            found = True
    if not found:
        print(f"Поиск по запросу '{searched_task}' не принес никаких результатов")


def save_tasks_to_file(filename="tasks.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)
    print(f"Задачи сохранены в файл '{filename}'")


def load_tasks_from_file(filename="tasks.json"):
    global tasks
    try:
        with open(filename, "r", encoding="utf-8") as file:
            tasks = json.load(file)
            print(f"Задачи загружены из файла '{filename}'")
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден. Создаю новый..")
        tasks = []


load_tasks_from_file()

while True:
    try:
        input_data = input("Действие:\nДобавить задачу(Д), Просмотр задач(Пр), Удаление задачи(У),"
                           "Изменение статуса(И), Поиск задачи(П), Выход(В)\n")

        if input_data.lower() == "д" or input_data.lower() == "l":
            add_task()
        elif input_data.lower() == "пр" or input_data.lower() == "gh":
            view_tasks()
        elif input_data.lower() == "у" or input_data.lower() == "e":
            del_task()
        elif input_data.lower() == "и" or input_data.lower() == "b":
            edit_task()
        elif input_data.lower() == "п" or input_data.lower() == "g":
            search_tasks()
        elif input_data.lower() == "в" or input_data.lower() == "d" or input_data.lower() == "exit":
            save_tasks_to_file()
            print("Выход..")
            break
    except KeyboardInterrupt:
        save_tasks_to_file()
        print(f"Неожиданное значение '{KeyboardInterrupt}'")
