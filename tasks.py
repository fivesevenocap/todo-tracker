from storage import save_tasks
from utils import get_valid_index
from datetime import datetime
import uuid
def add_task(tasks):
    name = input("Введите название задачи: ")
    task = {"Название задачи": name,
            "Статус": False, "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"), "id": str(uuid.uuid4())}
    tasks.append(task)
    save_tasks(tasks)
def show_tasks(tasks, sort_by_date = False):
    if not tasks:
        print("Список задач пуст")
        return
    if not sort_by_date:
        items_to_show = tasks
        print("Ваши задачи:")
    else:
        print("Ваши задачи по дате создания:")
        items_to_show = sorted(tasks, key=lambda x: x.get("created_at", ""), reverse=True)
    for n, task in enumerate(items_to_show, start = 1):
            status = "[x]" if task["Статус"] else "[ ]"
            task_id = task.get("id", "no-id")
            created = task.get("created_at", "дата неизвестна")
            print(f'{n}.{status} {task["Название задачи"]} (создано: {created}) id: {task_id}') 
def delete_tasks(tasks):
    index = get_valid_index(tasks, prompt = "Введите номер задачи для удаления: ")
    if index is None:
        return
    task = tasks[index]
    while True:
        choice = input(f"Вы уверены, что хотите удалить {task['Название задачи']}? (y/n): ")
        if choice == "y":
            removed = tasks.pop(index)
            save_tasks(tasks)
            print("Удалено:", removed["Название задачи"])
            break
        elif choice == "n":
            print("Операция прекращена")
            break
        else:
            print("Неверная команда")
    show_tasks(tasks)   
def toggle_tasks(tasks):
    index = get_valid_index(tasks, prompt = "Введите номер задачи для изменения статуса: ")
    if index is None:
        return
    tasks[index]["Статус"] = not tasks[index]["Статус"]
    save_tasks(tasks)
    print("Статус задачи обновлен")
    show_tasks(tasks)
def show_filtered(tasks, completed = True):
    if not tasks:
        print("Список задач пуст")
        return
    if completed:
        print("Выполненные задачи:")
    else:
        print("Невыполненные задачи:")
    found = False
    for n, task in enumerate(tasks, start = 1):
        status = "[x]" if task["Статус"] else "[ ]" 
        if task["Статус"] == completed:
            created = task.get("created_at", "дата неизвестна")
            task_id = task.get("id", "no-id")
            print(f'{n}.{status} {task["Название задачи"]} (создано: {created}) id: {task_id}')
            found = True
    if not found:
        if completed:
            print("Выполненных задач нет")   
        else:
            print("Невыполненных задач нет")
def rename_tasks(tasks):
    index = get_valid_index(tasks, prompt = "Введите номер задачи, которую хотите переименовать: ")
    if index is None:
        return
    task = tasks[index]
    while True:
        rename = input("Введите новое имя задачи: ")   
        clean = rename.strip()
        if not clean:
            print("Вы ничего не ввели")
        else:
            task["Название задачи"] = clean
            save_tasks(tasks)
            break
    show_tasks(tasks)  
def find_tasks(tasks):
    find = input("Введите слово для поиска задачи: ")
    clean_find = find.strip()
    if not clean_find:
            print("Вы ничего не ввели")
            return
    else:
        find_tr = False
        search_word = clean_find.lower()
        print("Вот что получилось найти:")
        for n, task in enumerate(tasks, start = 1):
            if search_word in task["Название задачи"].lower():
                status = "[x]" if task["Статус"] else "[ ]" 
                created = task.get("created_at", "дата неизвестна")
                task_id = task.get("id", "no-id")
                print(f'{n}.{status} {task["Название задачи"]} (создано: {created}) id: {task_id}')
                find_tr = True
        if not find_tr:
            print("Ничего не найдено")
def show_stats(tasks):
    if not tasks:
        print("Список задач пуст")
        return
    total = len(tasks)
    completed = 0
    for task in (tasks):
        if task["Статус"]:
            completed += 1
    uncompleted = total - completed
    perc = round(completed / total * 100)
    print(f"Всего задач: {total}")
    print(f"Выполненных задач: {completed}")
    print(f"Невыполненных задач: {uncompleted}")
    print(f"Процент выполнения: {perc}%")    