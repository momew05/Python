for i in range(1, 11, 1):
    print(i)

N = int(input(f'Введите число от 1 до 100\n'))
if N < 100:
    sum = 0
    i = 0
    while i <= N:
        sum += i
        i += 1
    print(f'Сумма чисел от 1 до {N}: {sum}')
else: print("не надо так")

N = int(input(f'Введите число от 1 до 100\n'))
if N < 100:
    for i in range (1, 11, 1):
        print(f'{N} * {i} = {N*i}')
else: print("не надо так")

str = input(f'Введите какую-нибудь строку\n')
if len(str) > 15:
    print("не надо так")
else:
    for c in str:
        print(c)


i = 0
while i <= 20:
    print(f'{i}', end=", ")
    i += 2

height = int(input(f'\nВведите высоту треугольника\n'))
if height > 15:
    print("не надо так")
else:
    i = 1
    while i <= height:
        str = ""
        while i <= height:
            str += "*"
            i += 1
            print(str)

