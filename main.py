# name = 'Maks'
# print('Hello', name)
# age = 20
# print(age)
# print(id(age))
# age = 'hello'
# print(age)

# a = b = c = 1
# print(a, b, c)

# a, b, c = 5, 'Hello', 9.2
# print(a, b, c)
#
# PI = 3.14
# print(PI)
# PI = 2
# print(PI)
#
# print(type(True))

# a = 1
# b = 2
# print('a =', a)
# print('b =', b)
# c = a
# a = b
# b = c
# print('a =', a)
# print('b =', b)
# a, b = b, a
# print('a =', a)
# print('b =', b)

# print('строка символов')
#
# number = 7 + 3 + 5
# print(number)
#
# number2 = 7 * 5 * 3
# print(number2)
#
# number3 = (5 + 7 + 3) / 3
# print(number3)

# num = 10
# num += 5
# print(num) #15

# num = 4321
# a = num % 10
# # print(a)
# num = num // 10
# # print(num)
# b = num % 10
# # print(b)
# num = num // 10
# # print(num)
# c = num % 10
# # print(c)
# num = num // 10
# # print(num)
# d = num % 10
# # print(d)
#
# print(a * 1000 + b * 100 + c * 10 + d)

# num = 4321
# res = num % 10 * 1000
# num //= 10
# res += num % 10 * 100
# num //= 10
# res += num % 10 * 10
# num //= 10
# res += num % 10
# print(res)

# Функции явного преобразования типов
# str()
# int()
# float()
# bool()

# num1 = '2.5'
# num2 = 3
# res = float(num1) + num2
# print(res)

# print(int(3.8))
# print(round(3.8))

# name = "Виктор"
# age = 28
# print("Меня зовут", name, ". Мне", age, "лет.", sep=" ", end=" ")
# print("Я учу Python.")

# name = input("Ваше имя: ")
# print(name)

# num = int(input("Введите число: "))
# num1 = int(input("Введите степень: "))
# st = num ** num1
# print("Число", num, "в степени", num1, "равно", st)

# b1 = True
# b2 = False

# print(bool("Python"))
# print(bool(""))  # False

# a = 10
# b = 5
# c = a == b
# print(a, b, c)

# print(5 - 3 == 2 and 1 + 3 == 4)

# cnt = 15
# if cnt < 10:
#     cnt += 1
# print(cnt)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещён")

# a = 15
# b = 15
# if a > b:
#     print("a > b")
# elif b > a:
#     print("b > a")
# else:
#     print("a == b")

# side1 = int(input("Введите первую сторону "))
# side2 = int(input("Введите вторую сторону "))
# side3 = int(input("Введите третью сторону "))
# if side1 == side2 == side3:
#     print("Треугольник равносторонний")
# elif side1 == side2 or side1 == side3 or side2 == side3:
#     print("Треугольник равнобедренный")
# else:
#     print("Треугольник разносторонний")

# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5:
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("понедельник")
# elif day == 6 or day == 7:
#     print("Выходной день")
# else:
#     print("Такого дня недели не существует")

# mon = int(input("Введите номер месяца: "))
# if mon == 12 or mon == 1 or mon == 2:
#     print("Время года зима")
# elif mon == 3 or mon == 4 or mon == 5:
#     print("Время года весна")
# elif mon == 6 or mon == 7 or mon == 8:
#     print("Время года Лето")
# elif mon == 9 or mon == 10 or mon == 11:
#     print("Время года Осень")
# else:
#     print("Ошибка ввода данных")

# crow = int(input("Введите количество ворон от 0 до 9: "))
# if crow == 0 or 5 <= crow <= 9:
#     print("На ветке", crow, "ворон")
# elif crow == 1:
#     print("На ветке", crow, "ворона")
# elif 2 <= crow <= 4:
#     print("На ветке", crow, "вороны")
# else:
#     print("Ошибка ввода")

# password = "qwerty"
#
# match password:
#     case 'admin':
#         print('Администратор')
#     case 'user':
#         print('Пользователь')
#     case 'moderator':
#         print('Модератор')
#     case _:
#         print('Пароль не верен')


# day = '1'
# time = 8
#
# match day:
#     case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница' if time >= 9:
#         print("Рабочий день")
#     case 'суббота' | 'воскресенье':
#         print("Выходной день")
#     case _:
#         print('Дня недели не существует или не рабочее время')

# a, b = 10, 20
#
# minim = a if a < b else b
# print(minim)

# a, b = 20, 10
# print("a == b" if a == b else "a > b" if a > b else "b > a")

# a = int(input("Введите делимое: "))
# b = int(input("Введите делитель: "))
# print(a // b if b != 0 else "На ноль делить нельзя")


# try:
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:
#     print("Что-то пошло не так")

# try: # попытаться выполнить
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError): # исключение
#     print("Нельзя вводить строки и делить на ноль")
# else: # когда в блоке try не возникло исключение
#     print("Все нормально. Вы ввели числа", n, "и", m)
# finally: # выполняется в любом случае
#     print("Конец программы")

# a = input("Введите первое число: ")
# b = input("Введите второе число: ")
# try:
#     a = int(a)
#     b = int(b)
# except ValueError:
#     a = str(a)
# finally:
#     print(a + b)

# Циклы

# i = 0
# while i < 5:
#     print("i =", i)
#     i += 1

# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print(i, end=" ")
#     i += 1

# a = int(input("Укажите количество символов: "))
# b = 0
# while a > b:
#     print("*", end=" ")
#     b += 1

# a = int(input("введите число: "))
# print("*" * a)

# a = int(input('Введите начало диапазона: '))
# b = int(input('Введите конец диапазона: '))
# if a % 2 == 0:
#     a += 1
# sum1 = 0
# while a <= b:
#     sum1 += a
#     a += 2
# print('Сумма: ', sum1)

# a = int(input('Введите начало диапазона: '))
# b = int(input('Введите конец диапазона: '))
# sum1 = 0
# if a > b:
#     a, b = b, a
# while a <= b:
#     if a % 2 != 0:
#         sum1 += a
#     a += 1
# print("Сумма нечетных: ", sum1)
#
# n = input("Введите целое число: ")
#
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число: ")
#
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# while True:
#     n = int(input("Введите положительное число: "))
#     if n < 0:
#         break

# pr = 1
# while True:
#     a = int(input("Введите число: "))
#     if a == 0:
#         break
#     pr *= a
# print("Результат: ", pr)

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print('Цикл окончен, i =', i)

# i = 1
# while i < 5:
#     print('Внешний цикл: i =', i)
#     j = 1
#     while j < 4:
#         print('\tВнутренний цикл: j =', j)
#         j += 1
#     i += 1

# a = 1
# while a < 10:
#     b = 1
#     while b < 10:
#         print(a, '*', b, '=', a * b, '\t\t', end='')
#         b += 1
#     print()
#     a += 1

# for element in collection:
#    тело цикла

# for i in "Hello", "red", "blue", "yellow", 20, 0.3:
#     print(i)

# print(range(5))

#  range(start, stop, step)

# for i in range(0, -8, -1):
#     print(i, end=" ")
# print()
# i = 10
# while i > 0:
#     print(i, end=" ")
#     i -= 1

# a = int(input("Введите целое число: "))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")

# for i in range(10, 100):
#     if i % 11 == 0:
#         print(i, end=" ")

# for i in range(3):
#     print(i, end=" ")
#     if i == 1:
#         break
# else:
#     print('\ndone')

# for i in range(3):
#     print("+++", i)
#     for j in range(2):
#         print("-----", j)

# w = int(input("Введите ширину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
# for i in range(h):
#     for j in range(w):
#         if i == 0 or j == 0 or i == h - 1 or j == w - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# letter = [i for i in "Hello"]
# print(letter)

# print([i for i in "Hello"])

# num = [i for i in range(30) if i % 2 == 0]
# print(num)

# Списки (list)

# nums = [8, 3, 9, 4, 1, "Hello", 2.3]
# print(nums)
# print(type(nums[1]))
# print(id(nums))
# print(nums[0])
# print(nums[-1])
#
#
# nums[-2] = 2
# nums[1] += 100
# print(nums)
# print(id(nums[1]))
# print(len(nums))

# s = []
# print(s)
# b = list()
# print(b)
#
# c = list("Hello")
# print(c)

# s = [5, 2] * 6
# print(s)
#
# a = [1, 2, 3]
# b = [4, 5]
# c = a + b
# print(c)

# n = list(range(2, 10, 2))
# print(n)

# [выражение for переменная in последовательность]

# n = 5
# a = [i ** 2 for i in range(1, n + 1)]
# print(a)

#  n = 5
# a = [i * 3 for i in "Hello"]
# print(a)

# a = [0] * int(input("Количество элементов в списке: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)

# a = [input("-> ") for i in range(int(input("Количество элементов в списке: ")))]
# print(a)

# nums = [8, 3, 9, 4, 1]
# print(nums * 2)
# for i in range(len(nums)):  # 0 1 2 3 4
#     print(nums[i] * 2, end=" ")
# print()
# for elem in nums:  # 8 3 9 4 1
#     print(elem * 2, end=" ")

# a = [int(input("-> ")) for i in range(int(input("Количество элементов в списке: ")))]
# summ = 0
# for i in a:
#     if i < 0:
#         summ += i
# print(summ)

# a = [i for i in range(21, 41)]
# summ = 0
# odd = 0
# for i in a:
#     if i % 2 != 0:
#         summ += i
#     else:
#         odd += 1
# print("Сумма нечетных элементов: ", summ, "\nКол-во четных: ", odd)

# a = [int(input("-> ")) for i in range(int(input("Количество элементов в списке: ")))]
# summ = 0
# sr = 0
# for i in a:
#     if i != 0:
#         summ += i
#         sr += 1
# print("Среднее: ", summ / sr)

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=" ")

# a = [9, 1, 3, 4, 5]
# print(a)
# a[0], a[-1] = a[-1], a[0]
# print(a)

# список[start:stop:step]

# a = [9, 4, 3, 1, 5, 17]
# print(a[1:4:2])
# print(a[:])

# a = list(range(1, 8))
# print(a)
# print(a[::-1])
# print(a[::2])
# print(a[1::2])
# print(a[0:1])
# print(a[-1:])
# print(a[3::4])
# print(a[4:])
# print(a[-3:1:-1])
# print(a[2:5])

# a = list(range(1, 8))
# print(a)
# a[1:3] = [0, 0, 0, 0]
# print(a)
# a[1:3] = [20]
# print(a)
# a[2] = 50
# print(a)
# a[3:5] = []
# print(a)
# del a[:]
# print(a)

# Методы списков
# a = list(range(1, 8))
# print(a)
# a.append(99)    # добавляет 1 элемент в конец списка
# print(a)
# a.extend([22, 11, 9])   # добавляет множество элементов в конец списка
# print(a)
# a.insert(0, 100)   # добавляет элемент в список по индексу
# print(a)
# a.extend('add')
# print(a)

# s = []
# n = int(input("Введите количество элементов в списке: "))
# for num in range(n):
#     x = input("-> ")
#     s.append(x)
# print(s)

# a = []
# b = int(input("Введите количество элементов списка: "))
# for i in range(b):
#     c = int(input("Введите число кратное 3: "))
#     if c % 3 == 0:
#         a.append(c)
#     else:
#         print(c, "не делится на 3 без остатся")
# print(a)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
# print(c)

# a = [1, 2, 3, 44, 55]
# b = [11, 22, 33]
# c = []
# if len(b) > len(a):
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
# print(c)

# b = [11, 12, 13, 2, 13, 4]
# b.remove(13)    # Удаляет элемент из списка по значению, если элементов несколько, то удаляется только первый
# print(b)
# a = 0
# if a in b:
#     b.remove(a)
# print(b)
#
# last = b.pop(1)  # с пустыми скобками - удаляет последний элемент из списка, с заданным индексом в скобках - удаление
# # по индексу
# print(b)
# print(last)
#
# b.clear()   # Очищает список
# print(b)

# a = [int(input("-> ")) for i in ' ' * int(input("Введите кол-во элементов: "))]
# b = int(input("Введите индекс: "))
# a.pop(b)
# print(a)

# a = [9, 2, 7, 2, 4, 2, 3, 2]
# num = a.count(2)    # кол-во заданных значений в списке
# print(num)
# ind = a.index(2, 4)     # возвращает первый индекс искомого значения. Можно указать значения start и end
# print(ind)

# a = [9, 2, 7, 2, 4, 2, 3, 2]
# b = a.copy()
# print("a:", a)
# print("b:", b)
# a.append(20)
# print("a:", a)
# print("b:", b)

# a = [9, 2, 7, 2, 4, 2, 3, 2]
# print(a)
# a.reverse()     # перестраивает элементы списка в обратном порядке
# print(a)
# a.sort()    # сортирует список по умолчанию - по возрастанию, reverse=True - по убыванию
# print(a)
#
# b = ["Виталий", "Сергей", "Александр", "Анна"]
# b.sort(key=len, reverse=True)
# print(b)

# c = sorted(a)
# print(c)

# Генерация случайных данных

# import random
#
# print(random.random())
# print(random.randint(2, 9))     # от 2 по 9 (включительно)
# print(random.randrange(2, 9, 2))

# from random import randint, randrange
#
# print(randint(2, 9))
# print(randrange(1, 9, 2))

# from random import *
#
# print(randint(2, 9))
# print(randrange(1, 9, 2))

# import random as r
#
# print(r.randint(2, 9))
# print(r.randrange(2, 9, 2))
# print(round(r.uniform(10.5, 25.5), 3))
#
# city = ["Москва", "Новосибирск", "Воронеж", "Сочи", "Екатеринбург"]
# # city = [1, 5, 4, 6, 7, 8, 9, 2, 3, 0]
# # print(r.choice(city))
# # print(r.choices(city, k=3))
# r.shuffle(city)
# print(city)

# import random as r

# mas = [r.randint(0, 100) for i in range(10)]
# print(mas)

# lst = [5, 3, 2, 4, 1]
# print(len(lst))
# print(max(lst))
# print(min(lst))
# print(sum(lst))

# s = [8, 9, 6, 4, 7, 8, 2, 3]
# res = []
# for i in s:
#     if i % 2 == 0:
#         res.append(i)
# print(res)

# x = list('1a2b3c4c')
# print(x)
# print('a' in x)
# print('w' in x)
# print('a' not in x)

# lst = []
# # if len(lst) == 0:
# # if not lst:
# #     print("Список пустой")
# print(bool(lst))

# from random import randint, randrange

# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
# a = [randint(0, 10) for i in range(n1)]
# b = [randint(0, 10) for j in range(n2)]
# print("Первый список: ", a)
# print("Второй список: ", b)
# c = a + b
# print("Третий список: ", c)
#
# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
# print("Элементы обоих списков без повторений: ", c)
#
# c = []
# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
# print("Элементы общие для двух списков: ", c)
#
# c = [min(a), min(b), max(a), max(b)]
# print("Минимальные и максимальные значения обоих списков: ", c)

# a = int(input("Введите размер списка: "))
# b = []
# while len(b) < a:
#     # i = randint(0, a - 1)
#     i = randrange(a)
#     if i not in b:
#         b.append(i)
# print(b)

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]

# print(m)
# print(m[1][2])

# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()

# for row in m:
#     # print(row)
#     for x in row:
#         print(x, end="\t")
#     print()

# w, h = 5, 3
# matrix = [[0 for x in range(w)] for y in range(h)]
# print([[x for x in row] for row in matrix])

# matrix = []
# for y in range(h):
#     new_row = []
#     for x in range(w):
#         new_row.append(0)
#     matrix.append(new_row)
# print(matrix)

# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()

# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, "+", y, "=", x + y)
#
# from random import randint

# w, h = 3, 4
# matrix = [[randint(0, 4) for x in range(w)] for y in range(h)]
# i = 1
# for row in matrix:
#     for x in row:
#         print(x, end="\t\t")
#         if x > 0:
#             i *= x
#     print()
# print("Произведение не нулевых элементов: ", i)

# w = h = 6
# i = 1
# matrix = [[randint(1, 100) for x in range(w)] for y in range(h)]
#
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()

# s = []
# # m = 101
# for i in range(w):
#     s.append(matrix[i][i])
#     if m > matrix[i][i]:
#         m = matrix[i][i]
# print(s)
# print(min(s))

# import math as m
# from math import sqrt, ceil, floor, pi

# num1 = sqrt(4)
# num2 = ceil(3.2)
# num3 = floor(3.8)
#
#
# print(num1)
# print(num2)
# print(num3)
#
# print(pi)

# r = int(input("Введите радиус окружности: "))
# print("Длина окружности: ", round(2 * pi * r, 2))
# print("Длина окружности: ", round(2 * pi * int(input("Введите радиус окружности: ")), 2))

# import time
# import locale
# locale.setlocale(locale.LC_ALL, "ru")
#
# seconds = time.time()
# print(seconds)
#
# local_time = time.ctime()
# print(local_time)
#
# res = time.localtime()
# print(res)
# print(res.tm_year)
#
# print(time.strftime("%d/%m/%Y, %H:%M:%S", time.localtime(4654414541)))
# print(time.strftime("Сегодня: %B %d, %Y"))

# pause = 5
# print("Program started...")
# time.sleep(pause)
# print(pause, "seconds")

# text = input("Название напоминания: ")
# local_time = float(input("Через сколько минут: "))
# local_time = local_time * 60
# time.sleep(local_time)
# print(text)

# start = time.time()
# time.sleep(5)
# finish = time.time()
# res = finish - start
# print(res, "sec.")

# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# res = finish - start
# print(res, "sec.")

#   Функции

# def hello(name, word):
#     print("Hello", name, ". Say ", word, sep="")
#
#
# hello("Irina", "hi")
# hello("Ivan", "hello")

# def get_sum(a, b):
#     print(a + b)
#
#
# x = 2
# y = 5
# get_sum(x, y)
# get_sum("abc", "def")


# def symbol(count, a, b):
#     # print((a + b) * (count // 2) + a * (count % 2))
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end="")
#         else:
#             print(b, end="")
#     print()
#
#
# symbol(9, "+", "-")
# symbol(7, "X", "0")

# def get_sum(a, b):
#     return a + b
#
#
# x = 2
# y = 5
# w = get_sum(x, y)
# print(w * 2)

# def maximum(one, two):
#     if one > two:
#         return True
#     else:
#         return False
#
#
# if maximum(5, 3):
#     print("Первое число больше")
# else:
#     print("Второе число больше")

# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         if 'a' <= ch <= 'z':
#             has_lower = True
#         if '0' <= ch <= '9':
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Этот пароль надежный")
# else:
#     print("Это ненадежный пароль")

# def cube(a):
#     return a * a * a
#
#
# for i in range(1, 11):
#     print(i, "в кубе =", cube(i))

# def change(lst):
#     # lst[0], lst[-1] = lst[-1], lst[0]
#     end = lst.pop()
#     start = lst.pop(0)
#     lst.insert(0, end)
#     lst.append(start)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))

# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 2, 5, 7))
# print(get_sum(1, 2, 5))
# print(get_sum(1, 2))
# print(get_sum(1, 2, d=5))

# def digits_sum(n, even=True):
#     s = 0
#     while n > 0:
#         cur_digit = n % 10
#         if even and cur_digit % 2 == 0:
#             s += cur_digit
#         if not even and cur_digit % 2 != 0:
#             s += cur_digit
#         n //= 10
#     return s
#
#
# print("Сумма четных цифр: ")
# print(digits_sum(9874023))
# print(digits_sum(38271))
# print(digits_sum(123456789))
# print("Сумма нечетных цифр: ")
# print(digits_sum(9874023, even=False))
# print(digits_sum(38271, even=False))
# print(digits_sum(123456789, even=False))

# def display_info(name, age):
#     print("Name: ", name, "\nAge", age)
#
#
# display_info("Ira", 23)
# display_info(23, "Ira")
# display_info(age=23, name="Ira")

#   Изменяемые и неизменяемые объекты

# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(lt1 == lt2)
# print(lt1 is lt2)
# print(id(lt1))
# print(id(lt2))
#
# a = 5
# b = 5
# print(a == b)
# print(a is b)
# print(id(a))
# print(id(b))

# lt1 = [1, 2, 3]
# print(id(lt1))
# lt1.append(4)
# print(lt1)
# print(id(lt1))

# s = True
# print(id(s))
# s = False
# print(s)
# print(id(s))

#   Кортеж (tuple)

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# a = 1, 2, 3, 4, 5
# print(type(a))
# print(a)
# b = tuple(a)
# print(type(b))
# print(b)

# t = tuple("Hello")
# print(type(t))
# print(t)
#
# print(t[1])
# print(t[1:3])

# s = tuple(input('-> ') for i in range(3))
# print(s)

# s = input("-> ")
# print(tuple(s))
# from random import randint

# s = tuple(2 ** i for i in range(1, 13))
# print(s)

# t1 = tuple("Hello")
# t2 = tuple("World")
# t3 = t1 + t2


# print(t3)
# print(len(t3))
#
# print(t3.count('l'))
# print(t3.count('a'))
# if 'a' in t3:
#     print(t3.index('a'))
# else:
#     print("Такого символа нет")

# for i in t3:
#     print(i, end=" ")

# def slicer(tpl, el):
#     while el in tpl:
#         first = tpl.index(el)
#         if tpl.count(el) == 1:
#             return tpl[first:]
#         if tpl.count(el) >= 2:
#             last = tpl.index(el, first + 1)
#             return tpl[first:last + 1]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# from random import randint


# def tup(tpl1, tpl2):
#     print(tpl1)
#     print(tpl2)
#     print(tpl1 + tpl2, "\n", "0 =", (tpl1 + tpl2).count(0))
#
#
# tup(tuple(randint(0, 5) for i in range(10)), tuple(randint(-5, 0) for j in range(10)))

# def tup(a, b):
#     return tuple(randint(a, b) for _ in range(10))
#
#
# tpl1 = tup(0, 5)
# tpl2 = tup(-5, 0)
#
# print(tpl1)
# print(tpl2)
# print(tpl1 + tpl2, "\n", "0 =", (tpl1 + tpl2).count(0))

# point = (10, 20)
#
# match point:
#     case (0, 0):
#         print("Точка находится в координатах 0:0")
#     case (x, 0):
#         print("Точка находится в координате", x, "по оси X и в координате 0 по оси Y")
#     case (0, y):
#         print("!!!Точка находится в координате 0 по оси X и в координате", y, "по оси Y")
#     case (x, y):
#         print("Точка находится в координате", x, "по оси X и в координате", y, "по оси Y")
#     case _:
#         print("Это не координаты точки")

# t = (10, 11, [1, 2, 3, ], [4, 5, 6], ['hello', 'world'])
# print(t, id(t))
# t[4][0] = 'new'
# t[4].append('hi')
# print(t, id(t))

# a = list(range(2))
# print(a)
# print(a.__sizeof__())
# b = list(range(10))
# print(b)
# print(b.__sizeof__())

#   Распаковка кортежей

# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t
# print(x, y, z)

# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# name1, age1, married1 = get_user()
# # name1, age1, married1 = user
# # user = get_user()
# # name1, age1, married1 = user
# print(name1, age1, married1)

# a = (1, 2)
# del a
# print(a)

# lst = [1, 2, 3, 4, 5, 6]
# print(lst)
# tpl = tuple(lst)
# print(tpl)
# lst = list(tpl)
# print(lst)

# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )
# print(countries)
# print()
# for country in countries:
#     countryName, countryPopulation, cities = country
#     print("\nСтрана:", countryName, "население =", countryPopulation)
#     for city in cities:
#         cityName, cityPopulation = city
#         print("\tГород:", cityName, "население =", cityPopulation)

# set() - множество

# s = {'banana', 'apple', 'orange', 'apple', 'orange'}
# print(s)
# print(type(s))
# print(len(s))

# c = ['red', 'green', 'green', 'blue']
# a = set(c)
# print(type(a))
# print(a)

# numbers = [1, 2, 2, 3, 3, 4, 4, 5, 6]
# s = list({x for x in numbers if x % 2 == 0})
# print(s)

# def to_set(a):
#     return set(a), len(set(a))
#
#
# print(to_set('я обычная строка'))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))
# # print(b)
# # print(c)

# s = {'banana', 'apple', 'orange'}
# print('apple' in s)
# print('apple' not in s)
# print(s)
# for i in s:
#     print(i)

# r = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# a = {i for i in r if 'a' not in i}
# b = {"A" + i[1:] if i[0] == 'a' else "B" + i[1:] for i in r}
# c = {"A" + i[1:] if i[0] == 'a' else "B" + i[1:] for i in r if i[1] == 'c'}
# print(a)
# print(b)
# print(c)
# for i in r:
#     if i[1] == 'c':
#         if i[0] == 'a':
#             print("A" + i[1:])
#         else:
#             print("B" + i[1:])

# s = {'banana', 'apple', 'orange'}
# s.add(4)  # Добавляет элемент во множество
# if 44 in s:
#     s.remove(44)  # Удаляет элемент по значению
# s.discard(4)  # Удаляет элемент по значению без генерации исключения
# s.pop()  # удаление первого элемента
# s.clear()  # полная очистка множества
# print(s)

#  Операции над множествами
# a = {0, 1, 2, 3, }
# b = {4, 3, 2, 1}
# # c = a.union(b)
# # c = a | b
# # a |= b
# c = a & b
# print(c)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
# s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# print(s)
# print('Unic elems count: ', len(s))
# print('max elem: ', max(s))
# print('min elem: ', min(s))

# a = set(input("Введите первую строку: "))
# b = set(input("Введите вторую строку: "))
# c = a & b
# print("Общими буквами являются: ", c)
# for i in c:
#     print(i, end=" ")

# a = set(input("Введите первую строку: "))
# b = set(input("Введите вторую строку: "))
# c = a - b
# for i in c:
#     print(i, end=" ")

# drawing = {"Марина", "Женя", "Света"}
# music = {"Костя", "Женя", "Илья"}
# one_hobby = drawing ^ music
# both_hobby = drawing & music
# print(one_hobby)
# print(both_hobby)
# print(drawing - music)

# s = frozenset([1, 2, 3, 4, 5])
# print(s)
#
# s1 = frozenset({'hello', 'world'})
# print(s1)

# Словарь (dict)

# a = [1, 2, 3]
# d = {'one': 1, 'two': 2, 'three': 3}
# print(a[0])
# print(d['one'])

#  d = {'one': 1, 'two': 2}
# d = dict(one=1, two=2)
# print(d)
# print(type(d))

# a = [
#     ('igor@mail.com', 'Igor'),
#     ('irina@mail.com', 'Irina'),
#     ('anna@mail.com', 'Anna'),
# ]
#
# b = dict(a)
# print(b)

# d = {i: 100 for i in range(2,7)}
# print(d)
# print(d[3])
# d[3] = 15
# print(d)

# d = {0: 'text', 'one': 45, (1, 2.3): "Кортеж", 42: [2, 3, 6, 7], True: {1, 0}}
# print(d)
# print(d[42][1])
# print(d[(1, 2.3)])
# d[(1, 2.3)] = "Новое значение"
# print(d)
# print("two" in d)
# key = 'one1'
# # if key in d:
# #     del d[key]
# try:
#     del d[key]
# except KeyError:
#     print("Элемента с ключом " + key + "нет в словаре")
# print(d)

# d = {0: 'text', 'one': 45, (1, 2.3): "Кортеж", 42: [2, 3, 6, 7], True: {1, 0}}
# print(d)
#
# for key in d:
#     print(key, " = ", d[key])

# a = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# b = 1
# for key in a:
#     b *= a[key]
# print(b)

# d = dict()
# d[1] = input('-> ')
# d[2] = input('-> ')
# d[3] = input('-> ')
# d[4] = input('-> ')
# d = {i: input("->") for i in range(1, 5)}
# print(d)
# dislike = int(input("Какой элемент исключить: "))
# del d[dislike]
# print(d)

# goods = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['Core i5-4670K', 3, 8500],
#     '3': ['AMD FX-6300', 6, 3700],
#     '4': ['Pentium G3220', 8, 2100],
#     '5': ['Core i5-3450', 5, 6400],
# }
#
# for i in goods:
#     print(i, ") ", goods[i][0], ' - ', goods[i][1], 'шт. по ', goods[i][2], 'руб', sep="")
#
# while True:
#     n = input('№: ')
#     if n != '0':
#         qty = int(input("Кол-во: "))
#         goods[n][1] = qty
#     else:
#         break
#
# for i in goods:
#     print(i, ") ", goods[i][0], ' - ', goods[i][1], 'шт. по ', goods[i][2], 'руб', sep="")

# d = {'a': 1, 'b': 2, 'c': 3}
# print(d['b'])
# value = d.get('c', 0)  # получить значение по заданному ключу
# print(value)
# n = d.keys()    # список ключей
# print(n)
# n = d.values()  # список значений
# print(n)
# n = d.items()   # список ключ + значение
# print(n)
#
# for i, j in d.items():
#     print(i, '->', j)

# d = {'a': 1, 'b': 2, 'c': 3}
#
# d2 = d.copy()   # создание копии словаря
#
# print("D =", d)
# print("D2 =", d2)
#
# d['b'] = 5
# d2['e'] = 7
#
# print("D =", d)
# print("D2 =", d2)

# d = {'a': 1, 'b': 2, 'c': 3}
# item = d.pop('b')   # удаляет элемент из словаря по ключу, возвращает значение ключа
# print(item)
# print(d)
# item = d.popitem()  # удаляет произвольную пару ключ + значение и возвращает их
# print(item)
# print(d)
# item = d.setdefault('f', 5)     # добавляет ключ со значение по умолчанию, если ключа не существует
# print(item)
# print(d)

# d.update({'a': 20, 'w': 10})    # обновление словаря
# print(d)
# d.update([('q', 7), ('t', 9)])
# print(d)

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# w = x дут y
# print(w)

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# w = x.copy()
# w.update(y)
# print(w)

# a = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}

# new_a = dict()
# new_a['name'] = a.pop('name')
# new_a['salary'] = a.pop('salary')
# new_a = {'name': a.pop('name'), 'salary': a.pop('salary')}
# print(a)
# print(new_a)

# a = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# # a.update({'location': a.pop('city')})
# a['location'] = a.pop('city')
# print(a)

# a = {
#     'first': {
#         1: 'one',
#         2: 'two',
#         3: 'three'
#     },
#     'second': {
#         4: 'four',
#         5: 'five'
#     }
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print('\t', y, ": ", a[x][y], sep="")

# a = {
#     'John': {'N': 3056, 'S': 8463, 'E': 8441, 'W': 2694},
#     'Tom': {'N': 4832, 'S': 6786, 'E': 4737, 'W': 3612},
#     'Anne': {'N': 5239, 'S': 4802, 'E': 5820, 'W': 1859},
#     'Fiona': {'N': 3904, 'S': 3645, 'E': 8821, 'W': 2451}
# }
# for x in a:
#     print(x)
#     for y in a[x]:
#         print(y, ': ', a[x][y], sep="")
#
# b = input("Имя: ")
# c = input("Регион: ")
# print(a[b][c])
# d = int(input("Новое значение: "))
# # a[b].update({c: d})
# a[b][c] = d
# print(a[b])

# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# print({k: v for k, v in d.items()})

# value = int(input("-> "))
# lt = [7, 8, 9, 10]
# d = {k: value for k in lt}
# print(d)

# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
#
# value = list(d.keys())
# print(value)
# value = list(d.values())
# print(value)
# value = list(d.items())
# print(value)

# a = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
#
# d = dict()
# s = None
#
# for i in a:
#     if type(i) == str:
#         d[i] = []   # d['one'] = []
#         s = i   # s = 'one'
#     else:
#         d[s].append(i)  # d['one']
# print(d)

# a = ['Dec', 'Jan', 'Feb']
# b = [12, 1, 2]
# d = dict(zip(a, b))
# print(d)

# one = {'name': 'Igor', 'last_name': 'Doe', 'Job': 'Consultant'}
# two = {'name': 'Irina', 'last_name': 'Smith', 'Job': 'Manager'}
#
#  for (k1, v1), (k2, v2) in zip(one.items(), two.items()):
#     print(k1, '->', v1)
#     print(k2, '->', v2)
#
# obj = {
#     'one': {'name': 'Igor', 'last_name': 'Doe', 'Job': 'Consultant'},
#     'two': {'name': 'Irina', 'last_name': 'Smith', 'Job': 'Manager'}
# }
# print(obj)

# pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# a, b = zip(*pairs)
# print(a)
# print(b)
#
# one = {'apple': 0.4, 'orange': 0.35}
# two = {'pepper': 0.2, 'onion': 0.55}
# print({**one, **two})

# data = ['a', 'b', 'c', 'd']

# for i in data:
#     print(i, end=' ')
# print()
# for i in range(len(data)):
#     print(i, end=' ')
# print()
#
# j = 1
#
# for i in data:
#     print(j, ":", i)
#     j += 1

# for j, i in enumerate(data, 1):
#     print(j, ':', i)

# n = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
#
# for j, (i, v) in enumerate(n.items(), 100):
#     print(j, ':', i, "->", v)

# a = [1, 2, 3]
# b = [4, *a, 5, 6]
# print(b)

# def func(*args):
#     res = 0
#     for i in args:
#         res += i
#     return res
#
#
# print(func(3, 2))
# print(func(3, 4, 6, 9, 5))
# print(func())


# def to_dict(*args):
#     print(*args)
#     print(args)
#     return {i: i for i in args}
#
#
# print(to_dict(1, 2, 3, 4, ))
# print(to_dict('grey', (2, 17), 3.11, -4))

# def fun(*args):
#     sa = 0
#     new_args = []
#     for i in args:
#         sa += i / len(args)
#     print(sa)
#     for i in args:
#         if i < sa:
#             new_args.append(i)
#     print(new_args, end=' ')
#     print()
#
#
# fun(1, 2, 3, 4, 5, 6, 7, 8, 9)
# fun(3, 6, 1, 9, 5)

# def func(a, *args):
#     return a, args
#
#
# print(func(2))
# print(func(2, 3, 4, 'abc'))

# def print_scores(student, *scores):
#     print('Student Name: ', student, end=', scores: ')
#     a, b = None, ""
#     for score in scores:
#         a = str(score) + ", "
#         b += a
#     print(b[:-2])
#
#
# print_scores("Kate", 100, 95, 88, 92, 99)
# print_scores("Rick", 96, 20, 33, 56)

# def reverse_num(n):
#     s = str(n)
#     return int(s[::-1])
#
#
# def func(*args, only_add=False):
#     res = []
#     for i in args:
#         if not only_add or only_add and i % 2:
#             res.append(reverse_num(i))
#     return res
#
#
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91))
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91, only_add=True))

# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(a='python'))


# def func(**data):
#     for key, value in data.items():
#         print(key, 'is', value)
#     print()
#
#
# func(name='Irina', surname="Sharma", age=22, phone=1234567890)
# func(name='Igor', surname="Wood", email="igor@mail.ru", country="Russia", age=25, phone=987654320)


# def db(**kwargs):
#     my_dict.update(kwargs)
#     print("my_dict =", my_dict)
#
#
# my_dict = {'one': 'first'}
# db(k1=22, k2=31, k3=11, k4=91)
# db(name='Bob', age=31, weight=61, eyes_color='grey')

# def func(a, *args, b=2, **kwargs):
#     print(a, args, kwargs, b)
#
#
# func(4, 5, 6, 7, k1=22, k2=31, k3=11, k4=91)

# Области видимости (scope)

# name = "Tom"  # Глобальная переменная
#
#
# def hi():
#     global name
#     name = 'Sam'    # локальные переменные
#     surname = 'Johnson'
#     print('Hello', name, surname)
#
#
# def bye():
#     print('Good bye', name)
#
#
# hi()
# bye()

# i = 5
#
#
# def func(arg=i):
#     print(arg)
#
#
# i = 6
# func()

# def add_two(a):
#     x = 2
#
#     def add_some():
#         return a + x
#
#     return add_some()
#
#
# print(add_two(3))

# import builtins
#
# name = dir(builtins)
#
# for t in name:
#     print(t)

# max = [8, 1, 2, 4, 5, 6, 9]
# print(min(max))
#
# a = [7, 8, 9, 5]
# print(max(a))

# def outer_func(who):
#     def inner_func():
#         print('Hello,', who)
#
#     inner_func()
#
#
# outer_func('World')

# def fun1():
#     a = 6
#
#     def fun2(b):
#         a = 4
#         print(a + b)
#
#     print('a =', a)
#     fun2(4)
#
#
# fun1()

# x = 25
# t = 0
#
#
# def fn():
#     global t
#     a = 30
#
#     def inner():
#         nonlocal a
#         a = 35
#
#     inner()
#     t = a
#
#
# fn()
# z = x + t
# print(z)

# def fn1():
#     x = 25
#
#     def fn2():
#         x = 33
#
#         def fn3():
#             nonlocal x
#             x = 55
#
#         fn3()
#         print('fn2.x =', x)
#
#     fn2()
#     print('fn1.x =', x)
#
#
# fn1()

# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# res = outer(2, 3, -1, 4)
# print(res)

# Замыкание

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# add = outer(5)
# print(add(10))
# print(add(20))
#
# add1 = outer(6)
# print(add1(10))
# print(outer(5)(10))

# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a
#         c.append(4)
#         a = a + 1
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())

# def func(city):
#     s = 0
#
#     def wrap():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return wrap
#
#
# res1 = func('Москва')
# res1()
# res1()
# res2 = func('Сочи')
# res2()
# res2()
# res1()

# students = {
#     'Alice': 98,
#     'Bob': 67,
#     'Chris': 85,
#     'David': 75,
#     'Ella': 54,
#     'Fiona': 35,
#     'Grace': 69
# }


# def classifier(lower, upper):
#     def student(exam):
#         return {k: v for k, v in exam.items() if lower <= v < upper}
#
#     return student
#
#
# A = classifier(80, 100)
# B = classifier(70, 80)
# C = classifier(50, 70)
# D = classifier(0, 50)
# print('A =', A(students))
# print('B =', B(students))
# print('C =', C(students))
# print('D=', D(students))

# def func(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def mul():
#         return a * b
#
#     def replace():
#         pass
#
#     replace.add = add
#     replace.sub = sub
#     replace.mul = mul
#     return replace
#
#
# obj1 = func(5, 2)
# print(obj1.add())
# print(obj1.sub())
# print(obj1.mul())

# lambda (Анонимные функции)

# print((lambda x, y: x + y)(1, 2))
# print((lambda x, y: x + y)('a', 'b'))
#
# func = lambda x, y: x + y
#
# print(func(1, 2))
# print(func('a', 'b'))

# print((lambda x, y: x ** 2 + y ** 2)(2, 5))

# summ = lambda a=1, b=2, c=3: a + b + c
#
# print(summ(10, 20, 30))
# print(summ(10, 20))
# print(summ(10))
# print(summ())

# func = lambda *args: args
#
# print(func(1, 2, 3, 4, 5, 6, 7))

# c = (lambda x: x * 2,
#      lambda x: x * 3,
#      lambda x: x * 4)
#
# for t in c:
#     print(t('abc_'))

# def inc(n):
#     return lambda x: n + x
#
#
# f = inc(42)
# print(f(3))
#
#
# def inc2(n):
#     def func(x):
#         return n + x
#
#     return func
#
#
# a = inc2(42)
# print(a(3))
#
# inc1 = (lambda n: lambda x: n + x)
#
# f1 = inc1(42)
# print(f1(3))
#
# print("!!!", (lambda n: lambda x: n + x)(42)(3))

# print((lambda a, b, c: a + b + c)(2, 4, 6))
# print((lambda d: lambda e: lambda f: d + e + f)(2)(4)(6))

# players = [
#     {'name': 'Антон', 'last name': 'Бирюков', 'rating': 9},
#     {'name': 'Алексей', 'last name': 'Бодня', 'rating': 10},
#     {'name': 'Федор', 'last name': 'Сидоров', 'rating': 4},
#     {'name': 'Михаил', 'last name': 'Семенов', 'rating': 6},
# ]
#
# res = sorted(players, key=lambda item: item['last name'])
# print(res)
#
# res = sorted(players, key=lambda item: item['rating'])
# print(res)
#
# res = sorted(players, key=lambda item: item['rating'], reverse=True)
# print(res)

# d = {'b': 15, 'a': 3, 'c': 7}
# lst = list(d.items())
# print(lst)
# lst.sort(key=lambda i: i[1])
# print(lst)
# print(dict(lst))

# a = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y), (lambda x, y: x / y)]
#
# print(a[3](12, 3))

# a = {'one': lambda x: x - 1, 'two': lambda x: x - 3, 'three': lambda x: x}
# b = [-3, 10, 0, 4]
#
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print(a['three'](i))

# d = {
#     1: lambda: print("Понедельник"),
#     2: lambda: print("Вторник"),
#     3: lambda: print("Среда"),
#     4: lambda: print("Четверг"),
#     5: lambda: print("Пятница"),
#     6: lambda: print("Суббота"),
#     7: lambda: print("Воскресенье")
# }
# d[3]()

# print((lambda a, b: a if a > b else b)(12, 5))

# print((lambda a, b, c: a if a < b and a < c else b if b < c and b < a else c)(9, 18, 15))

# map(func, iterable), filter(func, iterable)

# def mul(t):
#     return t * 2


# lst = [2, 8, 12, -5, 10]
#
# # lst2 = list(map(mul, lst))
# lst2 = list(map(lambda t: t * 2, lst))
# print(lst2)

# t = (2.88, -1.75, 100.03)
#
# # t2 = tuple(map(lambda x: int(x), t))
# t2 = tuple(map(int, t))
#
# print(t2)

# area = [3.45678, 5.676768, 4.001232, 7.45665, 1.4354566, 9.234232]
#
# res = list(map(round, area, [2, 2, 2, 2, 2, 2]))
# print(res)

# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
#
# res = list(map(lambda x, y: (x, y), st, num))
# print(res)

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# sum1 = list(map(lambda x, y: x + y, l1, l2))
# print(sum1)

# filter

# t = ('abcd', 'abc', 'adefg', 'def', 'ghi')
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)

# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# res = list(filter(lambda s: s > 75, b))
# print(res)

# from random import randint
#
# a = [randint(1, 40) for i in range(10)]
# print(a)
# b = list(filter(lambda i: 10 <= i <= 20, a))
# print(b)

# a = [45, 55, 60, 37, 100, 105, 220]
# b = list(filter(lambda i: i % 15 == 0, a))
# print(b)

# m = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(10))))
# print(m)

# Декораторы

# def hello():
#     return 'Hello, i am func "hello"'
#
#
# def super_func(func):
#     print('Hello, i am func "super_func"')
#     print(func())
#
#
# super_func(hello)

# def hello():
#     return 'Hello, i am func "hello"'
#
#
# test = hello
# print(test())

# def my_decorator(func):
#     def func_wrapper():
#         print('Code before')
#         func()
#         print('Code after')
#
#     return func_wrapper
#
#
# def func_test():
#     print('Hello, i am func "func_test')
#
#
# test = my_decorator(func_test)
# test()

# def my_decorator(func): # декорирующая функция
#     def func_wrapper():
#         print('*' * 40)
#         func()
#         print('*' * 40)
#
#     return func_wrapper
#
#
# @my_decorator   # декоратор
# def func_test():    # декорируемая функция
#     print('Hello, i am func "func_test')
#
#
# func_test()

# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
#
# @italic
# @bold
# def hello():
#     return "text"
#
#
# print(hello())

# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print("Вызов функции:", count)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()

# def args_decorator(fn):
#     def wrap(arg1, arg2):
#         print("Данные:", arg1, arg2)
#         fn(arg1, arg2)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#
#
# print_full_name("Ирина", "Назарова")

# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print("args:", args)
#         print("kwargs:", kwargs)
#         fn(*args, **kwargs)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#
#
# @args_decorator
# def print_full_name_1(first, second, last):
#     print("Меня зовут", first, second, last)
#
#
# print_full_name("Ирина", "Назарова")
# print()
# print_full_name_1("Виктор", "Федорович", "Назаров")

# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
#
# @decor("Сумма", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)

# def decor(x):
#     def func(fn):
#         def wrap(y):
#             print("Результат:", x * fn(y))
#
#         return wrap
#
#     return func
#
#
# @decor(3)
# def return_num(num):
#     return num
#
#
# return_num(5)

# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     raise TypeError("Некорректный тип данных", f_args[i])
#                     # return "Некорректный тип данных"
#             for k in kwargs:
#                 if type(f_kwargs[k]) != kwargs[k]:
#                     raise TypeError("Некорректный тип данных", f_kwargs[k])
#
#             return fn(*f_args, **f_kwargs)
#
#         return wrap
#
#     return wrapper
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x + y + z
#
#
# @typed(str, str, z=int)
# def typed_fn3(x, y, z="Hello!"):
#     return (x + y) * z
#
#
# print(typed_fn(3, 4, 5))
# # print(typed_fn(3, 4, "Doge"))
# print(typed_fn2("Hello", "World", "!"))
# print(typed_fn3("Hello", "World", z=5))

# def args_decorator(tx=None, decorator_text=""):
#     def my_decorator(func):
#         def wrap(*args):
#             print(decorator_text, end='')
#             func(*args)
#
#         return wrap
#
#     if tx is None:
#         return my_decorator
#     else:
#         return my_decorator(tx)
#
#
# @args_decorator(decorator_text="Hello, ")
# def hello_world(text):
#     print(text)
#
#
# @args_decorator
# def hello_world2(text):
#     print(text)
#
#
# hello_world("world!")
# hello_world2("Hi!")

# print('hello')

# print('Вносим изменения с клона')

# print(int('18'))
# print(int('18.5'))

# print(int('100', 2))
# print(int('100', 8))
# print(int('100', 10))
# print(int('100', 16))

# print(bin(18))  # 0b10010
# print(oct(18))  # 0o22
# print(hex(18))  # 0x12
#
# print(0b10010)
# print(0o22)
# print(0x12)

# q = 'Pyt'
# w = 'hon'
# e = q + w
# print(e)
# print(e * 2)
# print('q' in e)
#
# print(e[::-1])

# s = 'Python'
# s = s[:3] + 't' + s[4:]
# print(s)

# def change_char_to_str(s, c_old, c_new):
#     s2 = ''
#     for i in range(len(s)):
#         if s[i] == c_old:
#             s2 += c_new
#         else:
#             s2 += s[i]
#     return s2
#
#
# str1 = 'Я изучая Nython. Мне нравится Nython. Nython очень интересный язык программирования'
# str2 = change_char_to_str(str1, 'N', 'P')
# print(str1)
# print(str2)

# print(r'C:\folder\file.txt')    # r - подавление экранирования

# from math import pi
#
# name = 'Дмитрий'
# age = 25
# print(f'Меня зовут {name}. Мне {age} лет.')
# print(f'Значение числа pi: {round(pi, 2)}')
# print(f'Значение числа pi: {pi: .2f}')
#
# x = 5
# y = 10
# print(f'{x} x {y} / 2 = {x * y / 2}')
# print(f'{x = }, {y = }')

# a = 74
# print(f'{{{{{a}}}}}')

# dir_name = 'my_doc'
# file_name = 'data.txt'
# print(fr'home\{dir_name}\{file_name}')

# s = """<div>
#     <p>Текст</p>
# </div>
# """
# print(s)
# s1 = '''<div>
#     <p>Текст</p>
# </div>
# '''
# print(s1)

# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)   # __doc__ показывает документацию существующей функции
# print(sum.__doc__)

# import math
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return:  положительное число, площадь цилиндра
#     """
#     return 2 * math.pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)

# print(ord('a')) # ord - возвращает код символа

# while True:
#     n = input("-> ")
#     if n != '-1':
#         print(ord(n))
#     else:
#         break

# my_str = 'Test string for me'
# arr = [ord(x) for x in my_str]
# print('ASCII коды:', arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print('Среднее арифметическое:', arr)
# arr += [ord(x) for x in input("-> ")[:3] if ord(x) not in arr]
# print(arr)
# print(arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)

# print(chr(33))  # chr - возвращает символ по коду
# print(chr(122))

# 1)
# a = 122
# b = 97
# if a > b:
#     for i in range(b, a + 1):
#         print(chr(i), end=' ')
# else:
#     for i in range(a, b + 1):
#         print(chr(i), end=' ')

# 2)
# a = 122
# b = 97
# if a > b:
#     a, b = b, a
#     for i in range(a, b + 1):
#         print(chr(i), end=' ')

# print('apple' == 'Apple')
# print('apple' > 'Apple')
# print(ord("a"))
# print(ord('A'))
#
# print(9 > 5)
# print(ord('9'))
# print(ord('5'))

#
# from random import randint
#
#
# def random_password():
#     rand_len = randint(7, 10)
#     res = ''
#
#     for i in range(rand_len):
#         rand_char = chr(randint(33, 126))
#         res += rand_char
#     return res
#
#
# print('Ваш случайный пароль:', random_password())

# print(dir(str))

# s = 'hello, WORLD! I am learning Python.'
# print(s.capitalize())  # Hello, world! i am learning python.
# print(s.lower())  # hello, world! i am learning python.
# print(s.upper())  # HELLO, WORLD! I AM LEARNING PYTHON.
# print(s.swapcase())  # HELLO, world! i AM LEARNING pYTHON.

# print(s.count('h'))
#
# print(s.find('e'))  # поиск индекса элемента, возвращает "-1" если элемент не найден
# print(s.rfind('e'))  # поиск индекса элемента с правой стороны
#
# print(s.index('e1'))  # поиск индекса элемента, возвращает "ValueError" если элемент не найден
# print(s.rindex('e1'))

# a = 'один два'
# a = a[a.find(' ') + 1:] + ' ' + a[:a.find(' ')]
# print(a)

# s = 'ab12c59p7dq'
# digits = list(filter(lambda i: '0' <= i <= '9', s))
# print(digits)

# s = 'ab12c59p7dq'
# digits = []
# for ch in s:
#     if '0123456789'.find(ch) != -1:
#         digits.append(int(ch))
# print(digits)

# print('abc123'.isalnum())  # состоит ли строка из букв и цифр
# print('abc123!'.isalnum())
#
# print('ABCcbf'.isalpha())  # состоит ли строка из букв (любой регистр)
# print('123'.isdigit())  # состоит ли строка из цифр

# print('ру'.center(10, '-'))
# print('ру'.center(10, '-'))
# print('      py'.lstrip())
# print('py    '.rstrip())
# print('    py    '.strip())

# print('http://www.python.org'.lstrip('/:pths'))
# print(';py.$$$.'.rstrip(';$.'))
# print('http://www.python.org'.strip('/:pthsorgw.'))
# print('http://www.python.org'.lstrip('/:pths').rstrip('orgw.'))

# s = 'hello, WORLD! I am learning Python.'

# print(s.startswith('I am', 14))
# print(s.endswith('on.'))

# str1 = 'Я изучая Nython. Мне нравится Nython. Nython очень интересный язык программирования'
# print(str1.replace('Nython', 'Python'))

# s = 'Замените в этой строке все появления буквы "о" на букву "О", кроме первого и последнего вхождения'
# a = s[:s.find('о') + 1]
# b = s[s.find('о') + 1:s.rfind('о')]
# c = s[s.rfind('о'):]
# print(a + b.replace('о', 'О') + c)

# s = '-'
# seq = ('a', 'b', 'c')
# print(s.join(seq))
#
# print('..'.join(['1', '99']))
# print(':'.join('Hello'))
#
# print('Строка разделенная пробелами'.split())
# print('www.python.org.ru'.split('.', 2))
# print('www.python.org.ru'.rsplit('.', 2))

# a = input('-> ').split()
# a = list(map(int, a))
# print(a)

# a = input('Введите фамилию, имя и отчество: ').split()
# print(f'{a[0]} {a[1][0]}. {a[2][0]}.')

# Регулярные выражения

# import re

# print(dir(re))
# s = 'Я ищу совпадения в 2023 году. И я их найду в 2 счёта.'
# reg = 'Я ищу'
# print(re.findall(reg, s))  # возвращает список, содержащий все совпадения
# print(re.search(reg, s))  # возвращает первый найденный элемент по шаблону
# # print(re.search(reg, s).span())
# # print(re.search(reg, s).start())
# # print(re.search(reg, s).end())
# # print(re.search(reg, s).group())
# print(re.match(reg, s))  # возвращает первый найденный элемент по шаблону с начала строки
# reg = r'\.'
# print(re.split(reg, s)[:-1])  # возвращает список, в котором строка разбита по шаблону
# print(re.sub(reg, '!', s, 1))   # поиск и замена

# s = 'Я ищу совпадения в 2023 году. И я их найду в 2 счёта. [9875]'
# # reg = r'[А-яЁё.\[\]]'  # экранировать квадратные скобки
# reg = '[^А-я]'
# print(re.findall(reg, s))
# print(ord("Я"))
# print(ord("а"))

# s1 = "Час в 24-часовом формате от 00 до 23. 2021-06-15Т21:58. Минуты, в диапазоне от 00 до 59. 2021-06-15Т01:09."
# rg = r'[0-2][0-9]:[0-5][0-9]'
# print(re.findall(rg, s1))

# reg = r'20*'
# print(re.findall(reg, s))

# d = "Цифры: 7, +17, -42, 0012, 0.3"
# print(re.findall(r'[+-]?[\d.]+', d))

# d = '05-03-1987 # Дата рождения'
#
# print('Дата рождения: ', re.sub('-', '.', re.sub(r'#.*', '', d)))

# d = 'author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 1831'
# # reg = r'\w+\s*=\s*\w+\s*[\w.]+'
# reg = r'\w+\s*=[^;]+'
# print(re.findall(reg, d))

# s1 = '12 сентября 2023 года'
# reg = r'\d{2,4}'
# print(re.findall(reg, s1))

# d = '+7 499 456-45-78, +74994563578, 7 (499) 456 45 78, 74994564578'
# reg = r'\+*\d{4,}'
# print(re.findall(reg, d))

# s = 'Я ищу совпадения в 2023 году. И я их найду в 200000 - счёта. [98_75] Hello'
# reg = r'^\w+\s\w+'
# reg = r'\w+$'
# print(re.findall(reg, s))

# s = 'Hello, Привет'
# reg = r'^\w+\s\w+'
# print(re.findall(reg, s))
# print(ord('Я'))
# print(ord('а'))

# print(re.findall(r'\w+', '12 + й'))
# print(re.findall(r'\w+', '12 + й', re.A))

# text = 'hello world'
# print(re.findall(r'\w+', text, re.DEBUG))

# s = 'Я ищу совпадения в 2023 году. И я их найду в 200000 - счёта.'
# reg = 'я'
# print(re.findall(reg, s, re.IGNORECASE))

# text = """
# one
# two
# """

# print(re.findall(r'one.\w+', text))
# print(re.findall(r"one.\w+", text, re.DOTALL))
# print(re.findall(r'^two', text, re.MULTILINE))

# print(re.findall("""
# [a-z.-]+
# @
# [a-z.-]+
# """, "test@mail.ru", re.VERBOSE))

# text = """Python,
# python,
# PYTHON"""
# reg = '(?im)^python'
# print(re.findall(reg, text))

# def valid_name(name):
#     return re.findall("^[a-z0-9_-]{3,16}$", name, re.I)
#
#
# print(valid_name("Python_master"))
# print(valid_name("Python_master"))

# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall('<.*?>', text))

# s = "<p>Изображение <img alt='картинка' src='bg.jpg'> - фон страницы</p>"
# # reg = '<img.*?>'
# reg = r'<img\s+[^>]*src\s*=\s*[^>]+>'
# print(re.findall(reg, s))

# s = 'Петр, Ольга и Виталий'
# reg = 'Петр|Ольга|Виталий'
# print(re.findall(reg, s))

# s = 'int = 4, float = 4.0, double = 8.0f'
# # reg = r'\w+\s*=\s*\d+[.\w]*'
# reg = r'(?:int|double)\s*=\s*\d+[.\w]*'  # () -  сохраняющие скобки; (?:) - несохраняющие скобки
# print(re.findall(reg, s))

# # s = '127.0.0.1'
# s = '192.168.255.255'
# # reg = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
# # reg = r'[\d{1,3}\.]+' # разные варианты выполнения
# reg = r'(?:\d{1,3}\.){3}\d{1,3}'
# print(re.findall(reg, s)[0])

# s = "Word2016, PS6, AI5"
# reg = r'[a-z]+\d*'
# print(re.findall(reg, s, re.I))

# s = "5 + 7*2 - 4"
# reg = r'\s*[+*-]\s*'
# print(re.split(reg, s))

# a = input('-> ')
# reg = r'(0[1-9]|[12]\d|3[01])-(0[1-9]|1[0-2])-(19\d{2}|20\d{2})'
# print(re.findall(reg, a))

# s = 'Я ищу совпадения в 2023 году. И я их найду в 2 счёта.'
# reg = r'([0-9]+)\s(\D+)'
# print(re.findall(reg, s))
# print(re.search(reg, s).group())
# m = re.search(reg, s)
# print(m[0])
# print(m[1])
# print(m[2])

# text = """
# Самара
# Москва
# Тверь
# Уфа
# Казань
# """
# count = 0
#
#
# def repl_find(m):
#     global count
#     count += 1
#     return f"<option value='{count}'>{m.group(1)}</option>\n"
#
#
# print(re.sub(r'\s*(\w+)\s*', repl_find, text))

# s = "<p>Изображение <img alt='картинка' src='bg.jpg'> - фон страницы</p>"
# # reg = r'<img\s+[^>]*src\s*=\s*([\'"])(.+)\1>'
# reg = r'<img\s+[^>]*src\s*=\s*(?P<q>[\'"])(.+)(?P=q)>'
# print(re.findall(reg, s))

# (?P<name>...) (?P=name) имя круглой скобки

# s = "Самолет прилетает 10/23/2022. Будем рады вас видеть после 10/24/2022."  # 24.10.2022
# reg = r"(\d{2})/(\d{2})/(\d{4})"
# print(re.sub(reg, r'\2.\1.\3', s))

# s = "yandex.com and yandex.ru"  # http://yandex.com and http://yandex.ru
# reg = r"(([a-z0-9-]{2,}\.)+[a-z]{2,4})"
# print(re.sub(reg, r'http://\1', s))

# Рекурсия

# def elevator(n):
#     if n == 0:
#         print("Вы в подвале")
#         return
#     print("=>", n)
#     elevator(n - 1)
#     print(n, end=" ")
#
#
# n1 = int(input("На каком Вы этаже: "))
# elevator(n1)

# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res
#
#
# print(sum_list([1, 3, 5, 7, 9]))  # 25

# def sum_list(lst):
#     if len(lst) == 1:
#         return lst[0]
#     else:
#         return lst[0] + sum_list(lst[1:])
#
#
# print(sum_list([1, 3, 5, 7, 9]))  # 25

# def to_str(n, base):
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]
#     else:
#         return to_str(n // base, base) + convert[n % base]
#
#
# print(to_str(254, 16))

# names = ["Adam", ["Bob", ["Chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
# print(names[0])
# print(isinstance(names[0], list))
# print(names[1][1])
# print(isinstance(names[1][1], list))
# print(names[1][1][0])
# print(isinstance(names[1][1][0], list))
# print(names)


# def count_items(item_list):
#     count = 0
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#     return count
#
#
# print(count_items(names))

# count1 = 0
# for i in names:
#     if isinstance(i, list):
#         for j in i:
#             if isinstance(j, list):
#                 for k in j:
#                     count1 += 1
#             else:
#                 count1 += 1
#     else:
#         count1 += 1
# print(count1)


# def union(s):
#     if not s:
#         return s
#     if isinstance(s[0], list):
#         return union(s[0] + union(s[1:]))
#     return s[:1] + union(s[1:])
#
#
# print(union(names))

# def remove(text):
#     if not text:
#         return ""
#     if text[0] == "\t" or text[0] == " ":
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])
#
#
# print(remove(" Hello\tWorld! "))

# Линейный (последовательный) поиск
# from random import randint
#
# import time

#
#
# def seq_search(s, item):
#     found = False
#     pos = 0
#     stop = False
#     while pos < len(s) and not found and not stop:
#         if s[pos] == item:
#             found = True
#         else:
#             if s[pos] > item:
#                 stop = True
#             else:
#                 pos += 1
#     return found
#
#
# lst = [1, 2, 32, 8, 17, 19, 42, 13, 0]
# lst = [randint(1, 99) for i in range(100000)]
# start = time.monotonic()
# lst.sort()
# print(lst)
# print(seq_search(lst, 32))
# print(seq_search(lst, 0))
# res = time.monotonic() - start
# print(res, 'sec')

# Бинарный поиск

# def binary_search(s, item):
#     first = 0
#     last = len(s) - 1
#     found = False
#
#     while first <= last and not found:
#         midpoint = (first + last) // 2
#         if s[midpoint] == item:
#             found = True
#         else:
#             if item < s[midpoint]:
#                 last = midpoint - 1
#             else:
#                 first = midpoint + 1
#
#     return found
#
#
# lst = [0, 1, 2, 8, 13, 17, 19, 32, 42]
# print(binary_search(lst, 17))
# print(binary_search(lst, 3))

# Пузырьковая сортировка

# def bubble(array):
#     for i in range(len(array) - 1):
#         for j in range(len(array) - i - 1):
#             if array[j] > array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#         #     print(*array)
#         # print('=' * 50)
#
#
# lst = [randint(1, 99) for i in range(10000)]
# start = time.monotonic()
# # print(lst)
# bubble(lst)
# # print(lst)
# res = time.monotonic() - start
# print(round(res, 3), 'sec')

# Сортировка слияния

# def merge_sort(a):
#     n = len(a)
#     if n < 2:
#         return a
#
#     left = merge_sort(a[:n // 2])
#     right = merge_sort(a[n // 2: n])
#
#     i = j = 0
#     res = []
#
#     while i < len(left) or j < len(right):
#         if not i < len(left):
#             res.append(right[j])
#             j += 1
#         elif not j < len(right):
#             res.append(left[i])
#             i += 1
#         elif left[i] < right[j]:
#             res.append(left[i])
#             i += 1
#         else:
#             res.append(right[j])
#             j += 1
#     return res
#
#
# array = [randint(1, 99) for i in range(10000)]
# start = time.monotonic()
# # array = [8, 2, 6, 4, 5]
# # print(array)
# array = merge_sort(array)
# # print(array)
# res = time.monotonic() - start
# print(round(res, 3), 'sec')

# Сортировка Шелла

# def shell_sort(s):
#     gap = len(a)
#
#     while gap > 0:
#         for val in range(gap, len(s)):
#             cur_val = s[val]
#             pos = val
#
#             while pos >= gap and s[pos - gap] > cur_val:
#                 s[pos] = s[pos - gap]
#                 pos -= gap
#                 s[pos] = cur_val
#
#         gap //= 2
#     return s
#
#
# a = [randint(1, 99) for i in range(10000)]
# start = time.monotonic()
# # a = [10, 21, 9, 14, 67, 44, 26, 87]
# # print(a)
# shell_sort(a)
# # print(a)
# res = time.monotonic() - start
# print(round(res, 3), 'sec')

# Быстрая сортировка

# def quick_sort(a):
#     if len(a) > 1:
#         x = a[(len(a) - 1) // 2]
#
#         low = [i for i in a if i < x]
#         eq = [i for i in a if i == x]
#         hi = [i for i in a if i > x]
#         a = quick_sort(low) + eq + quick_sort(hi)
#
#     return a
#
#
# lst = [randint(1, 99) for i in range(10000)]
# start = time.monotonic()
# # lst = [9, 5, -3, 4, 7, 8, -8]
# # print(lst)
# # lst = quick_sort(lst)
# # print(lst)
# lst.sort()
# res = time.monotonic() - start
# print(round(res, 3), 'sec')

# Файлы

# f = open('text.txt')  # mode='r'
# print(*f)
# print(f)
# f.close()
# print(f.closed)

# f = open('text.txt')
# print(f.read(3))
# print(f.read())
# f.close()

# f = open('test.txt')
# # print(f.readline())
# # print(f.readline(8))
# # print(f.readline())
# # print(f.readline())
# print(f.readlines(26))
# print(f.readlines())
# f.close()

# i = 0
# f = open('test.txt')
# for line in f:
#     # print(line)
#     i += 1
# f.close()
# print(i)
#
# f = open('test.txt')
# print(len(f.readlines()))
# f.close()

# f = open('test1.txt', 'w')
# f.write('Hello\nWorld!')
# f.close()

# f = open('test1.txt', 'a')
# f.write('New text')
# f.close()

# f = open('xyz.txt', 'a')
# lines = ['\nThis is line 1', '\nThis is line 2']
# f.writelines(lines)
# f.close()

# f = open('xyz.txt', 'w')
# lst = [str(i ** 5) for i in range(1, 20)]
# for index in lst:
#     f.write(index + "\t")
# f.close()

# my_file = open('text2.txt', 'w')
# my_file.write('Заменить строку в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;')
# my_file.close()

# my_file = open('text2.txt', 'r')
# read_file = my_file.readlines()
# print(read_file)
# read_file[1] = 'Hello World!\n'
# print(read_file)
# my_file.close()
#
# my_file = open('text2.txt', 'w')
# my_file.writelines(read_file)
# my_file.close()

# my_file = open('text2.txt', 'r')
# delete_str = my_file.readlines()
# print(delete_str)
# num = int(input('-> '))
# delete_str.pop(num - 1)
# print(delete_str)
# my_file.close()
#
# my_file = open('text2.txt', 'w')
# my_file.write(''.join([*delete_str]))
# my_file.close()

# f = open('text.txt', 'r')
# print(f.read(3))
# print(f.tell())
# print(f.seek(1))
# print(f.read())
# print(f.tell())
# f.close()

# f = open('text.txt', 'w+')
# print(f.write('I am learning Python'))
# print(f.seek(3))
# print(f.write('-new string-'))
# print(f.tell())
# f.close()

# with open('text.txt', 'w+') as f:   # При таком способе открытия файла, закрывать его не нужно
#     print(f.write('12345\n67890'))
#
# with open('text.txt', 'r') as f:
#     for line in f:
#         print(line)

# file_name = 'res.txt'
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.77]
#
# with open(file_name, 'w+') as mf:
#     mf.write('\t'.join(map(str, lst)))

# with open(file_name, 'r+') as f:
#     float1 = f.read().split('\t')
#
# print(len(float1))
# print(f'Sum =  {sum(map(float, float1))}')

# def longest_word(file):
#     with open(file, 'r', encoding='utf-8') as text:
#         w = text.read().split()
#         max_length = len(max(w, key=len))
#         print(max_length)
#         print(w)
#         res = [word for word in w if len(word) == max_length]
#         if len(res) == 1:
#             return res[0]
#         return res
#
#
# print(longest_word('test.txt'))

# text = 'Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\n
# Строка №10\n'
#
# with open('one.txt', 'w') as f:
#     f.write(text)

# read_file = 'one.txt'
# write_file = 'two.txt'
#
# with open(read_file, 'r') as fr, open(write_file, 'w') as fw:
#     for line in fr:
#         line = line.replace('Строка', 'Линия - ')
#         fw.write(line)

# Модуль OS или OS.PATH

# import os
# import os.path

# print(os.getcwd())  # текущая директория
# print(os.listdir())  # список директорий и файлов по указанному пути

# os.mkdir('folder')  # создать папку
# os.makedirs('nested1/nested2/nested3')  # создает не только конечную директорию, но и промежуточные папки
# os.remove('xyz.txt')  # удаление файла
# os.rmdir('folder')  # удаление папки (пустой)
# os.rename('nested1', 'test')  # переименовывает файлы, папки и перемещает по заданному пути
# os.rename('two.txt', 'test/test1.txt')
# os.renames('text2.txt', 'text/test2.txt')   # переименовывает файлы, папки и перемещает по заданному пути, создавая
# промежуточные директории

# for root, dirs, files in os.walk('test', topdown=False):  # обходит дерево каталогов сверху вниз или снизу вверх
#     print('Root:', root)
#     print('Sub_dirs:', dirs)
#     print('Files:', files)

# def remove_empty_dirs(root_tree):
#     print(f'Удаление пустых директорий в ветви {root_tree}')
#     print('-' * 50)
#     for root, dirs, files in os.walk(root_tree):
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f'Директория {root} удалена')
#     print('-' * 50)
#
#
# remove_empty_dirs('test')

# print(os.path.split(r'D:\Python214\test\nested2\test1.txt'))    # разбивает путь на кортеж (head, tail)
#
# print(os.path.basename(r'D:\Python214\test\nested2\test1.txt'))
# print(os.path.dirname(r'D:\Python214\test\nested2\test1.txt'))

# print(os.path.join('nested2', r'D:\Python214', 'test1.txt'))    # соединяет один или несколько компонентов пути с
# учетом особенностей OS


# print(os.path.exists(r'D:\Python214\test\nested2\test1.txt'))   # возвращает True, если указанный путь существует

# import time
#
# path = r'D:\Python214\venv\Scripts\python.exe'
# print(os.path.getsize(path) // 1024)
# print(os.path.getmtime(path))  # последнее изменение файла
# print(os.path.getctime(path))  # создание файла
# print(os.path.getatime(path))  # последний доступ файла
#
# t = time.strftime('%d.%m.%Y, %H:%M:%S', time.localtime(os.path.getctime(path)))
# print(t)

# import os

# dirs = [r'Work\F1', r'Work\F2\F21']
# for d in dirs:
#     os.makedirs(d)

# files = {
#     'Work': ['w.txt'],
#     r'Work\F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#     r'Work\F2\F21': ['f211.txt', 'f212.txt']
# }
#
# for d, file in files.items():
#     for f in file:
#         file_path = os.path.join(d, f)
#         # print(file_path)
#         open(file_path, 'w').close()
#
# files_with_text = [r'Work\w.txt', r'Work\F1\f12.txt', r'Work\F2\F21\f211.txt', r'Work\F2\F21\f212.txt']
#
# for file in files_with_text:
#     with open(file, 'w') as f:
#         f.write(f'some sample text for {file} file')
#
#
# def print_tree(root, topdown):
#     print(f'Обход {root} {"сверху внизу" if topdown else "снизу вверх"}')
#     for root, dirs, fl in os.walk(root, topdown=topdown):
#         print(root)
#         print(dirs)
#         print(fl)
#     print("-" * 50)
#
#
# print_tree('Work', topdown=False)
# print_tree('Work', topdown=True)

# import os
# import time
# file_path = r'D:\Python214\Work\F2\F21\f212.txt'
#
# if os.path.exists(file_path):
#     dirs, name = os.path.split(file_path)
#     atime = os.path.getatime(file_path)
#     print(f'{name} ({dirs}) - время последнего доступа к файлу: '
#           f'{time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(atime))}')
# else:
#     print(f'Файл {file_path} не существует!')

# print(os.path.isfile(r'D:\Python214\Work\w.txt'))
# print(os.path.isdir(r'D:\Python214\Work'))

# dir_name = 'test'
#
# objs = os.listdir(dir_name)
# print(objs)
#
# for obj in objs:
#     p = os.path.join(dir_name, obj)
#     if os.path.isfile(p):
#         print(f'{obj} - file - {os.path.getsize(p)} bytes')
#     elif os.path.isdir(p):
#         print(f'{obj} - dir')

# class Point:
#     x = 1
#     y = 1
#
#
# p1 = Point()
# print(p1.x)
# print(type(p1))
# print(dir(Point))
