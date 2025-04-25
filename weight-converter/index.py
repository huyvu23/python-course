weight = int(input('Weight: '))
unit = input('(L)bs or (K)gs: ')

if unit.upper() == 'L':
    converted = int(weight) * 0.45
    print('Weight in Kgs:', converted)
elif unit.upper() == 'K':
    converted = int(weight) / 0.45
    print('Weight in Lbs:', converted)
else:
    print('Please enter a valid unit (L or K)')