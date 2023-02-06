contents = [
    'All carrots are to be sliced longitudinally',
    'The carrots were reportedly sliced',
    'The slicing process was well presented'
]

filenames = ['doc.txt', 'report.txt', 'presentation.txt']

# zip returns n-length tuples until the number of iterables passed to zip are exhausted
for content, filename in zip(contents, filenames):
    file = open(f'../files/{filename}', 'w')
    file.write(content)
    
a = "I am a string on my own"
