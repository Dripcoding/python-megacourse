import json
 
 
with open('questions.json', 'r') as file:
    content = file.read() # load content as string

data = json.loads(content) # load content as list of dictionaries


for question in data:
    print(question['question_text'])
    for idx, alternative in enumerate(question['alternatives']):
        print(f'{idx + 1} - {alternative}')
    user_choice = int(input('Enter your answer: '))
    question['user_choice'] = user_choice

score = 0

for idx, question in enumerate(data):
    if question['user_choice'] == question['correct_answer']:
        score += 1
    message = f"{idx + 1} - Your answer: {question['user_choice']}, Correct answer: {question['correct_answer']}"
    print(message)

print(f'user score is {score} / {len(data)}')

    