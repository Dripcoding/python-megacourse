# Coding Exercise 2
# ips = ['100.122.133.105', '100.122.133.111']

# Copy-paste the ips list in a .py file and extend the program so it:

# 1. Prompts the user to input an index (e.g, 0 or 1).
# 2. Returns the IP address that has that index.

ips = ['100.122.133.105', '100.122.133.111']

idx = int(input("please provide a 0 or 1 "))

print(f'You chose {ips[idx]}')