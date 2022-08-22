# №1

# try:
#     from sys import argv
#     """При использовании терминала"""
#     script_name, working_time, salary, bonus = argv
#
#     working_time = int(working_time)
#     salary = int(salary)
#     bonus = int(bonus)
#
#     result = (working_time * salary) + bonus
#     print(f"Заработная плата сотрудника составляет {result}")
# except ValueError:
#     print("В терминале все работает")

# №2

# spisok = [2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# new_one = [x for y, x in enumerate(spisok) if spisok[y - 1] < spisok[y]]
#
# print(f"Исходный список: {spisok}")
# print(f"Новый список: {new_one}")

# №3

# print(f" Числа от 20 до 240 кратные 20 или 21 - {[el for el in range(20,241) if el % 20 == 0 or el % 21 == 0]}")

# №4

# spisok = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# new_spisok = [el for el in spisok if spisok.count(el) < 2]
#
# print(f"Исходный список: {spisok}")
# print(f"Новый список: {new_spisok}")

# №5

# from functools import reduce
#
# def my_funk (x,y):
#     return (x*y)
#
# print(f"Вывод четных чисел: {[el for el in range(99,1001) if el%2 ==0]}")
#
# print(f"Вывод произведения чисел: {[reduce(my_funk, [el for el in range(99,1001) if el%2 ==0])]}")

# №6

# from itertools import count, cycle

# for a in count(int(input("Введите число: "))):
#     if a == 11:
#         break
#     print(a)

# spisok = [1, 2, 5, 'Hello', "world", 9.34, None]
# count = 0
#
# for b in cycle(spisok):
#     if count > 10:
#         break
#     print(b)
#     count += 1

# №7
# from math import factorial

# def fact(n):
#     k = 1
#     if k < 0:
#         print("Требуется только положительные значения!")
#     else:
#         for el in range(1, n + 1):
#             k = k * el
#             yield k
# z = int(input("Введите число: "))
# for x in fact(z):
#     print(f"Факториал равен: {x}")
