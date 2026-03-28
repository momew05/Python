number = input("введите целое положительное число\n")
sum = 0
for x in str(number):
    sum += int(x)
print(f"Сумма цифр числа {number} = {sum}")

stroka = input("введите любую строку\n")
digitsum = 0
alphasum = 0
othersum = 0
for x in stroka:
    if x.isdigit():
        digitsum += 1
    elif x.isalpha():
        alphasum += 1
    else:
        othersum += 1
print(f"Статистика строки:\n Всего цифр: {digitsum}\n Всего букв: {alphasum}\n Всего других символов: {othersum}")

for i in range(1, 11):
    for j in range(1, 11):
        if j*i < 50:
            print(j*i, end=" ")
        else: break
    print()

# :)
k_1 = ["свободна"]