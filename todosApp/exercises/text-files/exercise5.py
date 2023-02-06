# Please download the three text files a.txt, b.txt, and c.txt from the resources. 
# Then, create a program that reads each text file and prints out the content of each in the command line.  

filenames = ['a.txt', 'b.txt', 'c.txt']

for file in filenames:
    file = open(file, 'r')
    print(file.read())
    file.close()