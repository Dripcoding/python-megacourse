date = input("enter today's date: ")
mood = input('how do you rate your mood today from 1 to 10: ')
thoughts = input("let your thoughts flow: \n")

# use with context manager to perform file operations without worrying about closing
with open(f'../journal/{date}.txt', 'w') as file:
    # all file operations in this block
    file.write(mood + '\n\n')
    file.write(thoughts)