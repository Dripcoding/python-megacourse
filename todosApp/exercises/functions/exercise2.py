# The function we wrote in exercise 1 returned 9.7.  
# Change the function so this time it returns Max: 9.7, Min: 9.2 where 9.7 is the maximum and 9.2 is the minimum

def get_max():
    grades = [9.6, 9.2, 9.7]
    max_value, min_value = max(grades), min(grades)
    return f'Max: {max_value}, Min: {min_value}'


print(get_max())

