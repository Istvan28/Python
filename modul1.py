
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
        result += f"{task_id}: {task_values['title']} | {task_values['desc']} | {task_values['priority_text']} | {task_values['status']}\n"
    return result

def priority_def():
    try:
           while True:
            priority = int(input("Выберите приоритет задачи (1 - низкий, 2 - средний, 3 - высокий): "))
            if priority == 1:
                priority_text = "низкий"
                break
            elif priority == 2:
                priority_text = "средний"
                break
            elif priority == 3:
                priority_text = "высокий"
                break
            else:
              print("Пожалуйста, введите цифру от 1 до 3.")
    except ValueError:
         print("Пожалуйста, введите допустимое число.")
         save_task(priority_text)

def status_def():
     while True:
        try:
            status = int(input("Выберите статус важности задачи (1 - низкий, 2 - средний, 3 - высокий): "))
            if status == 1:
                return "низкий"
            elif status == 2:
                return "средний"
            elif status == 3:
                return "высокий"
            else:
                print("Пожалуйста, введите цифру от 1 до 3.")
        except ValueError:
            print("Пожалуйста, введите допустимое число.")
   
          
          

def create_task(task_id):
            title = input("Введи название: ")
            desc = input("Введи описание: ")
            priority_text = priority_def()
            status = status_def()
            save_task(tasks)
            return {task_id: {"title": title, "desc": desc, "priority_text": priority_text, "status": status}}

          

def view_task():
     with open("tasks.txt", "r") as file:
          content = file.read()
          print(content)

def delete_task():
     view_task()
     delete_choice = int(input("Введи ID задачи: "))
     with open("tasks.txt", "w") as file:
          pass
     print("Задача удалена")
     

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
            print("3. Пgосмотреть задачу")
            print("4. Удалить задачи")
            print("5. Поиск(Введите ключевое слово: )")
            print("6. Выход")
            user_choice = int(input("Выбери действие: "))
            if user_choice == 1:
                gen_task(tasks)
                print("Задача создана.")
            # elif user_choice == 2:
            elif user_choice == 3:
                view_task()
            elif user_choice == 4:
                delete_task()
        except ValueError:
            print("Введи номер задачи!!!")

ask()






    
    
    


