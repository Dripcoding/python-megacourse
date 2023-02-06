
# With that in mind, your task for this exercise 
# is to extend the program you created in Exercise 1 by displaying a message to the user when they enter 0 for the "total value"

try:
    total_value = float(input('Enter total value: '))
    value = float(input('Enter value: '))
    print(f'That is {(value / total_value) * 100}%')
except ValueError:
    print('You need to enter a number. Run the program again.')
except ZeroDivisionError:
    print('Your total value cannot be 0')