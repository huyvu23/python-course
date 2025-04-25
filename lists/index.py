names = ['index', 'index2']
names.sort()
names.append('index3')
print(names[0])
print(names[1:])
print(names)

numbers = [1, 2, 3, 4, 5]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)
