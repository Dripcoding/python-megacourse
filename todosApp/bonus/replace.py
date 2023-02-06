filenames = ['1.Raw Data.txt', '2.Reports.txt', '3.Presentations.txt']

for filename in filenames:
    # strings are immutable
    new = filename.replace('.', '-', 1) # string to replace, replacement, which occurence
    idx = filenames.index(filename)
    filenames[idx] = new

print(filenames)

# tuple - collection that is ordered and immutable

filenames2 = ('1.Raw Data.txt', '2.Reports.txt', '3.Presentations.txt')

print(filenames2)