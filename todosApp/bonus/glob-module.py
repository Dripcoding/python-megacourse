import glob

myfiles = glob.glob('bonus/globs/*.txt') # filenames you want to find by the given pattern

# access the content of each file and do something
for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read())


