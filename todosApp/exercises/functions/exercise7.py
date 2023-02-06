# Write a program that gets a list of names from the user and returns the number of names given. 
# You are encouraged to use a function. Here is how the program would work:

def count_names(names):
    return len(names.split(','))


names = input('Enter names separated by commas (no spaces): ')

print(f'You provided {count_names(names)} names')