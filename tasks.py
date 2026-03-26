from storage import save_tasks
from utils import get_valid_index
from datetime import datetime
import uuid
def add_task(tasks):
    name = input("Введите название задачи: ")
    mapping = {"1": "high", "2": "medium", "3": "low"}
    while True:
        print("Выберите приоритет для этой задачи:")
        print("1 - High")
        print("2 - Medium")
        print("3 - Low")
        choice = input("Ваш выбор: ")
        priority = mapping.get(choice)
        if priority:
            print("Вы присвоили статус: ", priority)
            break
        else:
            print("Некорректная команда")
    deadline = input("Введите дедлайн (например: 2026-03-30) или оставьте пустым: ")
    clean_deadline = deadline.strip()
    if not clean_deadline:
        print("Дедлайн не присвоен")
        clean_deadline = None
    else:
        print("Вы ввели дату дедлайна:", clean_deadline)
    task = {"Название задачи": name, "Статус": False, "priority": priority, "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"), "deadline": clean_deadline, "id": str(uuid.uuid4())}
    tasks.append(task)
    save_tasks(tasks)
def print_task(task, n):
    grades = {"high": "[H]", "medium": "[M]", "low": "[L]"}
    priority = task.get("priority", "medium")
    priority_mark = grades.get(priority, "[M]")
    status = "[x]" if task["Статус"] else "[ ]"
    created = task.get("created_at", "дата неизвестна")
    task_id = task.get("id", "no-id")
    deadline = task.get("deadline", "Нет")
    print(f'{n}.{priority_mark}{status} {task["Название задачи"]} (создано: {created}) (Дедлайн: {deadline}) id: {task_id}')
def show_tasks(tasks, sort_by_date = False, sort_by_priority = False):
    if not tasks:
        print("Список задач пуст")
        return
    if sort_by_date and sort_by_priority:
        print("Выберите только один тип сортировки")
        return
    if sort_by_date:
        print("Ваши задачи по дате создания:")
        items_to_show = sorted(tasks, key=lambda x: x.get("created_at", ""), reverse=True)
    elif sort_by_priority:
        priority_order = {"high": 0, "medium": 1, "low": 2}    
        items_to_show = sorted(tasks, key=lambda task: priority_order.get(task.get("priority", "medium")))   
        print("Задачи по приоритету (high → medium → low):")
    else:
        items_to_show = tasks
        print("Ваши задачи:")
    for n, task in enumerate(items_to_show, start = 1):
        print_task(task, n)
def delete_tasks(tasks):
    show_tasks(tasks)
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
        if task["Статус"] == completed:
            print_task(task, n)
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
                print_task(task, n)
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
def show_by_priority(tasks, priority):
    if not tasks:
        print("Список задач пуст")
        return
    found = False
    titles = {"high": "высоким", "medium": "средним", "low": "низким"}
    print(f"Задачи с {titles.get(priority)} приоритетом:")
    for n, task in enumerate(tasks, start = 1):
        task_priority = task.get("priority", "medium")
        if task_priority == priority:
            print_task(task,n)
            found = True
    if not found:
        print("Задач с таким приоритетом не найдено")
def change_priority(tasks):
    show_tasks(tasks)
    mapping = {"1": "high", "2": "medium", "3": "low"}
    index = get_valid_index(tasks, prompt="Введите номер задачи: ")
    if index is None:
        return
    while True:
        print("Выберите новый приоритет для этой задачи:")
        print("1 - High")
        print("2 - Medium")
        print("3 - Low")
        choice = input("Ваш выбор: ")
        priority = mapping.get(choice)
        if priority:
            tasks[index]["priority"] = priority
            save_tasks(tasks)
            print("Приоритет обновлен")
            break
        else:
            print("Некорректная команда")
def show_overdue_tasks(tasks):
    today = datetime.now().strftime("%Y-%m-%d")
    found = False
    for n, task in enumerate(tasks, start = 1):
        deadline = task.get("deadline", None)
        if deadline is not None and today > deadline and not task["Статус"]:
            print_task(task,n)
            found = True
    if not found:
            print("Нет просроченных задач")
def show_tasks_for_today(tasks):
    today = datetime.now().strftime("%Y-%m-%d")
    found = False
    for n, task in enumerate(tasks, start = 1):
        deadline = task.get("deadline", None)
        if deadline is not None and today == deadline and not task["Статус"]:
            print_task(task,n)
            found = True
    if not found:
            print("Нет задач на сегодня")    