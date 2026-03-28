import random as ran

def greet(name):
    print(f'Привет, {name}! Добро пожаловать')

greet("Лиза")
greet("Маша")
greet("Борис")

def calculate_area(width, height):
    s = width*height
    return s

w = int(input("Введите ширину\n"))
h = int(input("Введите высоту\n"))

print(f'Площадь равна: {calculate_area(w, h)}')

is_even = lambda number: True if number % 2 == 0 else False

for i in range(1, 11, 1):
    if is_even(i):
        print(f'Число {i} четное')
    else:
        print(f'Число {i} нечетное')

def usd_to_rub(usd, cur = 90):
    rub = usd * cur
    return rub

print(f'90 долларов это {usd_to_rub(90)} рублей')
print(f'90 долларов это {usd_to_rub(90, 88)} рублей по курсу 88')

def get_max(x, y):
    if x > y:
        return x
    elif y > x:
        return y
    else:
        return "Числа равны"

print(get_max(5, 8))
print(get_max(8, 5))
print(get_max(5, 5))

def analyze_list(lst):
    maximum = max(lst)
    minimum = min(lst)
    sum = 0
    for num in lst:
        sum += num
    return f'Максимальное число: {maximum}, минимальное число {minimum}, сумма чисел в списке: {sum}'

array = []
for i in range(0, 16):
    array.append(ran.randint(0, 100))

print(analyze_list(array))