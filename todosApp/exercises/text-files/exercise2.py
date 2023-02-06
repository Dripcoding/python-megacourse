# Write a program that reads the essay.txt file and returns the number of characters contained in the file. 

file = open('essay.txt', 'r')

text = file.read()

print(f'number of characters in file is {len(text)}')

file.close()