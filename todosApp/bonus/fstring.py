waiting_list = ['sen', 'ben', 'john']
waiting_list.sort() # sort alphaabetically
waiting_list.sort(reverse=True) # sort in reverse

for idx, item in enumerate(waiting_list):
    row = f'{idx + 1}.{item.capitalize()}'
    print(row)
    
    