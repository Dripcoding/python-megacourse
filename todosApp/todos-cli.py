# from './modules/functions.py' import get_todos, write_todos
# import functions # imports entire module
# from modules import functions # import functions module from modules dir

import functions
import time

now = time.strftime('%b %d, %Y %H:%M:%S')

print(now)

while True:
    user_action = input('Type add, show, edit, complete or exit: ').strip()

    if user_action.startswith('add'): 
        todo = user_action[4:]
        
        print(f'adding {todo} as a todo item')
        
        todos = functions.get_todos(filepath='todos.txt')
        
        todos.append(todo  + '\n')
        
        functions.write_todos(filepath='todos.txt', todos_arg=todos) # order of arguments doesn't matter here
        
    elif user_action.startswith('show'):
        todos = functions.get_todos('todos.txt')
            
        for idx, item in enumerate(todos):
            item = item.strip('\n')
            print(f'{idx + 1} - {item}')
        print(f'you have {len(todos)} todos remaining') 
            
    elif user_action.startswith('exit'):
        break
    
    elif user_action.startswith('edit'):
        try:
            todos = functions.get_todos('todos.txt')
            
            number = int(user_action[5:])
            
            todos[number - 1] = input("Enter new todo: ") + '\n'
            
            functions.write_todos(todos, 'todos.txt') # order of args matter

        except ValueError:
            print('Your command is not valid')
            continue
            
    elif user_action.startswith('complete'): 
        try:
            todos = functions.get_todos('todos.txt')
            
            number = int(user_action[9:])
            idx = number - 1
            todo_to_remove = todos[idx].strip('\n')
            todos.pop(idx)
            
            functions.write_todos(todos) # args with defaults can be omitted
                
            print(f"todo {todo_to_remove} was removed from your list")
        except IndexError:
            print('There is not item with that number')
            continue
        
    elif user_action.startswith('debug'):
        todos = functions.get_todos('todos.txt')
        
        print(list(enumerate(todos)))
    
    else:
        print("Command is not valid")
