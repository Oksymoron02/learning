import json
import os

filename = "tasks.json"

def save_tasks(tasks):
    with open(filename, "w") as file:
        json.dump(tasks, file)

def load_tasks():
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    else:
        return []

def add_task():
    title = input("Podaj treść zadania: ")
    task = {
        "title": title,
        "done": False
    }
    tasks.append(task)
    save_tasks(tasks)

def show_tasks():
    print("Twoje zadania: ")
    for index, task in enumerate(tasks, start=1):
        status = "[x]" if task["done"] else "[ ]"
        print(f"{index}. {status} {task['title']}")

def mark_task_done():
    show_tasks()
    selected = int(input("Które zadanie odhaczyć?: "))
    if 0 < selected <= len(tasks):
        tasks[selected - 1]["done"] = True
    show_tasks()
    save_tasks(tasks)

def delete_task():
    show_tasks()
    selected = int(input("Które zadanie usunąć?: "))
    if 0 < selected <= len(tasks):
        del tasks[selected - 1]
    else:
        print("Nieprawidłowy numer zadania.")

    save_tasks(tasks)
    print("Zadanie usunięte.")
    
tasks = load_tasks()

while True:
    print()
    print("Wybierz opcję: ")
    print("1. Dodaj zadanie")
    print("2. Pokaż zadania")
    print("3. Oznacz jako wykonane")
    print("4. Usuń zadanie")
    print("5. Wyjdź")
    print()

    wybór = int(input("Twój wybór: "))

    if wybór == 1:
        add_task()
    elif wybór == 2:
        show_tasks()
    elif wybór == 3:
        mark_task_done()
    elif wybór == 4:
        delete_task()
    elif wybór == 5:
        break
    else:
        print("Nieprrawidłowy wybór, spróbuj ponownie.")