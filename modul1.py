
tasks = {}

def gen_id(tasks):
    if not len(tasks):
        return 1
    return max(tasks.keys()) + 1

def save_task(tasks):
    with open("tasks.txt", "w") as file:
        file.write(tasks_to_strings(tasks))

def tasks_to_strings(tasks):
    result = ""
    for task_id, task_values in tasks.items():
        result += f"{task_id}: {task_values['title']} | {task_values['desc']} | {task_values['priority']} | {task_values['status']}\n"
    return result

def priority_def():
    try:
           while True:
            priority = int(input("Выберите приоритет задачи (1 - low, 2 - middle, 3 - high): "))
            if priority == 1:
                return "low"
            elif priority == 2:
                return "middle"
            elif priority == 3:
                return "high"
            else:
              print("Пожалуйста, введите цифру от 1 до 3.")
    except ValueError:
         print("Пожалуйста, введите допустимое число.")
         save_task(priority)

def status_def():
     while True:
        try:
            status = int(input("Выберите статус важности задачи (1 - low, 2 - middle, 3 - high): "))
            if status == 1:
                return "low"
            elif status == 2:
                return "middle"
            elif status == 3:
                return "high"
            else:
                print("Пожалуйста, введите цифру от 1 до 3.")
        except ValueError:
            print("Пожалуйста, введите допустимое число.")
   
def create_task(task_id):
            title = input("Введи название: ")
            desc = input("Введи описание: ")
            priority = priority_def()
            status = status_def()
            save_task(tasks)
            return {task_id: {"title": title, "desc": desc, "priority": priority, "status": status}}

def view_task():
     with open("tasks.txt", "r") as file:
          content = file.read()
          print(content)

def delete_task():
     view_task()
     try:
         delete_choice = int(input("Введи ID задачи: "))
         if delete_choice in tasks:
             del tasks[delete_choice]
             save_task(tasks)
             print(f"Задача с ID {delete_choice} удалена.")
         else:
             print("Задача с таким ID не найдена.")
     except ValueError:
         print("Введите число.")

def update_task():
    view_task()
    try:
        update = int(input("Введите ID задачи: "))
        if update in tasks:
             new_title = input("Введите новое название задачи: ")
             new_desc = input("Введите новое описание задачи: ")
             priority = priority_def()
             status = status_def()
             tasks[update] = {
                 "title": new_title,
                 "desc": new_desc,
                 "priority": priority,
                 "status": status
             }

             with open("tasks.txt", "w") as file:
                 content = save_task(tasks)
                 file.write.__str__(content)
                 print(f"Изменено {content}")
        else:
            print("Задача с таким ID не найдена.")
    except ValueError:
        print("Введи число.")
    except TypeError:
        print("Обновлено")

def gen_task(tasks):
    task_id = gen_id(tasks)
    data = create_task(task_id)
    tasks.update(data)
    save_task(tasks)

def ask():
    while True:
        try:
            print("1. Создать задачу")
            print("2. Обновить задачу")
            print("3. Просмотреть задачу")
            print("4. Удалить задачи")
            print("5. Поиск(Введите ключевое слово: )")
            print("6. Выход")
            user_choice = int(input("Выбери действие: "))
            if user_choice == 1:
                gen_task(tasks)
                print("Задача создана.")
            elif user_choice == 2:
                update_task()
            elif user_choice == 3:
                view_task()
            elif user_choice == 4:
                delete_task()
            # elif user_choice == 5:

            elif user_choice == 6:
                print("Вы вышли ")
                break
        except ValueError:
            print("Введи номер задачи!!!")

ask()






    
    
    


