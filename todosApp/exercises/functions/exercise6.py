# Your task for this exercise is to use the function you created in exercise 1. 
# Then, below the function definition, get the year of birth from the user using an input function and 
# then call and print the defined function to get the user's age as output. Here is how the program should behave:

def calculate_user_age(year_of_birth, current_year=2023):
    return current_year - year_of_birth


birth_year = int(input('What is your year of birth? '))
age = calculate_user_age(birth_year)

if age > 120:
    print("Wow you've lived a long life!")
else:
    print(f'User age is {age}')
