# A client wants to buy a coin-flip probability program from you.

# The programs should work like this:

# 1. The user runs the program. The program asks the user to enter "head" or "tail".  
# The user flips a coin on their desk, table, floor, etc., and then enters "head" or "tail". The user does the same over and over again.

# In each cycle, the program should return the current percentage of heads in the program, similar to what you see in the screenshot above. 
# Also, you should write each user entry (i.e., head or tail) in a text file using a with-context manager, one entry per line.


head_count = 0
tail_count = 0


while True:    
    choice = input('please enter head or tail: ')

    match choice:
        case 'head':
            head_count += 1
        case 'tail':
            tail_count += 1
    
    percentage_of_heads = float(head_count / (head_count + tail_count))
            
    print(f'Heads: {float(percentage_of_heads) * 100}%')
            
    with open('heads-tails.txt', 'a') as file:
        file.write(choice + '\n')

