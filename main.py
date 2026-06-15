import json


def load_data():
    with open("tasks.json", 'r') as file:
        data = json.load(file)
    return data


def check_tasks(data):
    if len(data["tasks"]) > 0:
        print("Задачи:\n")
        for task in data["tasks"]:
            print(f'[{task["id"]}] {task["name"]}')
        print(f"\nВсего задач: {len(data["tasks"])}")
    else:
        print("Задач нет!")


def add_task(data):

    user_task = str(input("Введите задачу: "))

    data["tasks"].append({
        'id': len(data['tasks']) + 1,
        'name': user_task, 
        'done': False
        })
    with open("tasks.json", 'w') as file:
        json.dump(data, file, indent=4)
    print("\nЗадача успешно записана!")


def delete_task(data):
    if len(data["tasks"]) > 0:
        while True:
            for index, task in enumerate(data["tasks"]):
                print(f'[{index + 1}] {task["name"]}')
                
            user_task_choice = int(input())
            
            for task in data["tasks"]:
                if user_task_choice == task["id"]:
                    data['tasks'].remove(task)
                    
            with open("tasks.json", 'w') as file:
                json.dump(data, file, indent=4)
            print("Задача успешно удалена!")
            break
    else:
        print("Задач нет!")


def compited_task(data):
   while True:
        for index, task in enumerate(data["tasks"]):
            print(f'[{index + 1}] {task["name"]}')

        user_task_choice = int(input())
                
        for task in data["tasks"]:
            if user_task_choice == task["id"]:
                task['done'] = True
                with open("tasks.json", 'w') as file:
                    json.dump(data, file, indent=4)
                print('\nЗадача выполнена!') 
        break 


def main():
  
    data = load_data()
    
    while True: 
        print("\nПункт управления") 
        print("\n[1] Добавить задачу") 
        print("[2] Посмотреть задачи")
        print("[3] Удалить задачу задачу")
        print("[4] Выход") 
        
        user_choice = int(input()) 
        
        if user_choice == 1:  
            add_task(data)

        elif user_choice == 2:
            check_tasks(data)
  
        elif user_choice == 3:
            delete_task(data)

        elif user_choice == 4: 
            print("Досвидания!") 
            break


if __name__ == '__main__':
	main()