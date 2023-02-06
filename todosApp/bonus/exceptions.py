# interpreter can't detect logical errors pertaining to the program requirements

try:
    width = float(input('Enter rectangle width: '))
    length = float(input('Enter rectangle length: '))
    
    # this scenario doesn't match the program requirements but is valid from the interpreter's perspective 
    if width == length:
        exit('That looks like a square')

    area = width * length
    print(area)
except ValueError:
    print('Please enter a number')