def get_valid_index(tasks, prompt = "Введите номер задачи"):
    if not tasks:
        print("Список задач пуст")
        return None
    while True:
        try:
            choice = int(input(prompt))
            index = choice - 1
            if 0 <= index < len(tasks):    
                return index       
            else:
                print("Ошибка. Введите номер от 1 до", len(tasks))
        except ValueError:
            print("Ошибка ввода") 