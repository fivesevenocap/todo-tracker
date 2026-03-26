from storage import save_tasks, load_tasks
from utils import get_valid_index
from tasks import add_task, show_tasks, delete_tasks, toggle_tasks, show_filtered, rename_tasks, find_tasks, show_stats, show_by_priority, change_priority, show_overdue_tasks, show_tasks_for_today
def main():
    tasks = load_tasks()
    while True:
        print("1 - Добавить задачу")
        print("2 - Показать все задачи")
        print("3 - Удалить задачу")
        print("4 - Отметить выполненной")
        print("5 - Показать выполненные задачи")
        print("6 - Показать невыполненные задачи")
        print("7 - Показать отсортированные по датам задачи")
        print("8 - Переименовать задачу")
        print("9 - Найти задачу по слову")
        print("10 - Фильтр задач по приоритету")
        print("11 - Показать статистику задач")
        print("12 - Показать задачи по приоритету (high → medium → low)")
        print("13 - Изменить приоритет задачи")
        print("14 - Показать просроченные задачи")
        print("15 - Показать задачи на сегодня")
        print("0 - Выход")
        choice = input("Ваш выбор: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            delete_tasks(tasks)
        elif choice == "4":
            toggle_tasks(tasks)
        elif choice == "5":
            show_filtered(tasks, completed = True)
        elif choice == "6":
            show_filtered(tasks, completed = False)
        elif choice == "7":
            show_tasks(tasks,sort_by_date = True)
        elif choice == "8":
            rename_tasks(tasks)
        elif choice == "9":
            find_tasks(tasks)
        elif choice == "10":
            mapping = {"1": "high", "2": "medium", "3": "low"}
            print("1 - Показать задачи с высоким приоритетом")
            print("2 - Показать задачи со средним приоритетом")
            print("3 - Показать задачи с низким приоритетом")
            ch = input("Ваш выбор: ")
            priority = mapping.get(ch)
            if priority:
                show_by_priority(tasks, priority)
            else:
                print("Неверная команда")
        elif choice == "11":
            show_stats(tasks)
        elif choice == "12":
            show_tasks(tasks,sort_by_priority = True)
        elif choice == "13":
            change_priority(tasks)
        elif choice == "14":
            show_overdue_tasks(tasks)
        elif choice == "15":
            show_tasks_for_today(tasks)
        elif choice == "0":
            break
        else:
            print("Некорректная команда")
    print("Спасибо!")
if __name__ == "__main__":
    main()