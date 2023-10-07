# Задание 1
a = int(input("Введите число "))
b = int(input("Введите число "))
for i in range(a, b):
    if i % 7 == 0:
        print(i)
# Задание 2
c = int(input("Введите число "))
d = int(input("Введите число "))
print('все числа диапазона')
for i in range(c, d+1):
    print(i)
print('Вывод в убывающем порядке')
for i in range(d, c-1, -1):
    print(i)
print('все числа кратные 7')
for i in range(c, d+1):
    if i % 7 == 0:
        print(i)
print('количество чисел, кратных 5')
count = 0
for i in range(c, d+1):
    if i % 5 == 0:
        count += 1
print(count)
# Задание 4
f = int(input('Введите число '))
g = int(input('Введите число '))
for i in range(f, g+1):
    if i % 3 == 0:
        print('Число кратно 3', 'Fizz')
for i in range(f, g+1):
    if i % 5 == 0:
        print('Число кратно 5', 'Buzz')
for i in range(f, g+1):
    if i % 3 == 0 and i % 5 == 0:
        print('Число кратно 3 и 5', 'Fizz Buzz')
for i in range(f, g+1):
    if i % 3 != 0 and i % 5 != 0:
        print(i)