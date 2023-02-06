import functions
import PySimpleGUI as sg
import time
import os

# generate file on 1st app load
if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        pass

# ===== SETTING UP GUI =====
sg.theme('Black')

clock_label = sg.Text('', key='clock')
label = sg.Text('Type in a to-do')
input = sg.InputText(tooltip='Enter todo', key='todo')
add_button = sg.Button('Add', mouseover_colors='LightBlue2',
                       tooltip='Add your todo')
list_box = sg.Listbox(values=functions.get_todos(), 
                      key='todos',
                      enable_events=True, 
                      size=[45, 10])
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit')

row0 = [clock_label]
row1 = [label]
row2 = [input, add_button]
row3 = [list_box, edit_button, complete_button]
row4 = [exit_button]

window = sg.Window('My To-Do App', 
                   layout=[row0, row1, row2, row3, row4], 
                   font=('Helvetica', 20))

# ===== TODOS LOGIC =====
while True:
    event, values = window.read(timeout=200) # type: ignore # show window with data
    window['clock'].update(value=time.strftime('%b %d, %Y %H:%M:%S'))
    
    # print(event)
    # print(values)
    
    match event:
        case 'Add':
            todos = functions.get_todos()
            todos.append(values['todo'] + '\n')
            functions.write_todos(todos)

            window['todos'].update(values=todos)
        case 'Edit':
            try:
                selected = values['todos'][0]
                new_todo = values['todo']
                
                todos = functions.get_todos()
                idx = todos.index(selected)
                todos[idx] = new_todo + '\n'
                
                functions.write_todos(todos)

                window['todos'].update(values=todos)
            except IndexError:
                sg.popup('Please select a todo before editing it.', 
                         font=('Helvetica', 20))
        case 'Complete':
            try:    
                selected = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(selected)
                
                functions.write_todos(todos)
                
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup('Please select a todo before editing it.', 
                         font=('Helvetica', 20))
        case 'Exit':
            break
        case 'todos':
            current_value = values['todos'][0]
            window['todo'].update(value=current_value)
        case sg.WIN_CLOSED:
            break;

window.close() # close window when user closes application