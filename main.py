import json


def load_data():
    with open("tasks.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def check_tasks(data):
    print("-" * 25)
    if len(data["tasks"]) > 0:
        print("Задачи:\n")
        for index, task in enumerate(data["tasks"]):
            print(f'[{index + 1}] {task["name"]}')
        print(f"\nВсего задач: {len(data["tasks"])}")
    else:
        print("Задач нет!")
    print("-" * 25)


def add_task(data):
    print("-" * 25)
    user_task = str(input("Введите задачу: "))

    data["tasks"].append({
        'id': len(data['tasks']) + 1,
        'name': user_task, 
        'done': False
        })
    with open("tasks.json", 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print("\nЗадача успешно записана!")
    print("-" * 25)


def delete_task(data):
    print("-" * 25)
    if len(data["tasks"]) > 0:
        while True:
            for index, task in enumerate(data["tasks"]):
                print(f'[{index + 1}] {task["name"]}')
                
            user_task_choice = int(input("\nВыберите задачу, которую хотите удалить: "))
            
            for index, task in enumerate(data["tasks"]):
                if user_task_choice == index + 1:
                    data['tasks'].remove(task)
                else:
                    continue
                    
            with open("tasks.json", 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
            print("\nЗадача успешно удалена!")
            break
    else:
        print("Задач нет!")
    print("-" * 25)


def completed_task(data):
    print('-' * 25)
    if len(data["tasks"]) > 0:
        while True:
            for index, task in enumerate(data["tasks"]):
                print(f'[{index + 1}] {task["name"]}')

            user_task_choice = int(input('Выберите задачу, которую хотите отметить как "выполненную": '))
                    
            for task in data["tasks"]:
                if user_task_choice == task["id"]:
                    task['done'] = True
                    with open("tasks.json", 'w', encoding="utf-8") as file:
                        json.dump(data, file, indent=4, ensure_ascii=False)
                    print('\nЗадача выполнена!') 
            break
    else:
        print("Задач нет!")
    print('-' * 25)

def delete_all_tasks(data):
    data["tasks"].clear()
    with open("tasks.json", 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print("\nЗадачи успешно удалены!")

def main():

    data = load_data()

    while True: 
        print("\nПункт управления") 
        print("\n[1] Добавить задачу") 
        print("[2] Посмотреть задачи")
        print("[3] Отметить выполненную задачу")
        print("[4] Удалить задачу задачу")
        print("[5] Удалить все задачи")
        print("[6] Выход") 

        user_choice = int(input("\nВыберите действие: ")) 

        if user_choice == 1:  
            add_task(data)

        elif user_choice == 2:
            check_tasks(data)
            
        elif user_choice == 3:
            completed_task(data)

        elif user_choice == 4:
            delete_task(data)

        elif user_choice == 5:
            delete_all_tasks(data)

        elif user_choice == 6: 
            print("\nДосвидания!") 
            break


if __name__ == '__main__':
	main()