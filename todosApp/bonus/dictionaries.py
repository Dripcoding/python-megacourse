# password strength checker

password = input('Enter a new password: ')

result = {}

if len(password) >= 8:
    # result.append(True)
    result['length'] = True
else:
    result['length'] = False
    
digit = False
for i in password:
    if i.isdigit():
        digit = True
        break

result['digits'] = digit
        
uppercase = False
for i in password:
    if i.isupper():
        uppercase = True
        break

result['uppercase'] = uppercase

print(f'result is {result}')
print(f'result values are {result.values()}')
print(f'result keys are {result.keys()}')

if all(result.values()): # return True if all items in iterable eval to True
    print('Strong Password')
else:
    print('Weak Password')