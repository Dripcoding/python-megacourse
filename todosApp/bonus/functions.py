def get_average():
    with open('data.txt', 'r') as file:
        data = file.readlines()

    values = data[1:]
    values = [float(value) for value in values]
    return sum(values) / len(values)

average = get_average()
print(average)