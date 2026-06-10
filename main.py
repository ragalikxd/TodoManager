import json

def load_data():
    with open("tasks.json", 'r') as file:
        data = json.load(file)
    return data

def add_task(user_task, data):
 
    data["tasks"].append({
        'id': len(data['tasks']) + 1,
        'name': user_task, 
        'done': False
        })
    
    with open("tasks.json", 'w') as file:
        json.dump(data, file, indent=4)


def read_tasks():
	with open("tasks.json", 'r') as file:
		data = json.load(file)
	return data["tasks"]


def main():
  
    data = load_data()
    
    while True: 
        print("\nПунктц управления") 
        print("[1] Добавить задачу") 
        print("[2] Посмотреть задачи") 
        print("[3] Выход") 
        
        user_choice = int(input()) 
        
        if user_choice == 1: 
            user_task = str(input("Введите задачу: ")) 
            add_task(user_task, data) 
            print("Задача успешно записана!") 
        elif user_choice == 2: 
            print(read_tasks()) 
        elif user_choice == 3: 
            print("Досвидания!") 
            break



if __name__ == '__main__':
	main()