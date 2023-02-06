import random

# Your task is to create a program that generates a random whole number.

# As you can see, the program first asks the user to enter a whole number. 
# Then, once the user enters a number, the program asks the user again to enter another number.
# Then, the program returns a random number that falls between the two whole numbers.

def get_random_number(lower, upper):
    return random.randrange(lower, upper)

lower_bound = int(input('Enter the lower bound: '))
upper_bound = int(input('Enter the upper bound: '))

print(get_random_number(lower_bound, upper_bound))