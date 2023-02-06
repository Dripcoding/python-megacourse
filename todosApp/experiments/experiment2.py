user_prompt = "Enter a todo: "

todos = []

while True:
    todo = input(user_prompt).title() # capitalize first letter of every word
    todos.append(todo) # add todo to the list
    print(todos)