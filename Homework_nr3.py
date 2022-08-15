# №1

# def my_funk (*args):
#     try:
#         x = int(input("Введите первое число: "))
#         y = int(input("Введите второе число: "))
#         z = x / y
#     except ZeroDivisionError:
#         return ("Ошибка! На ноль делить нельзя!")
#
#     return (z)
#
# print(my_funk())


# №2

# name = input("Введите имя: ")
# surname = input("Введите фамилию: ")
# birthday = str(input("Введите день рождения: "))
# city = input("Введите город проживания: ")
# e_mail = input("Введите адрес электронной почты: ")
# mob_nr = input("Введите мобильный телефон: ")
#
#
# spisok_info = ["name", "surname", "birthday", "city", "e_mail", "mob_nr"]
# spisok_par = dict.fromkeys(spisok_info)
#
# def my_funk (name, surname, birthday, city, e_mail, mob_nr):
#     spisok_par["name"] = name
#     spisok_par["surname"] = surname
#     spisok_par["birthday"] = birthday
#     spisok_par["city"] = city
#     spisok_par["e_mail"] = e_mail
#     spisok_par["mob_nr"] = mob_nr
#     print(spisok_par)
#
# my_funk(name, surname, birthday, city, e_mail, mob_nr)


# №3

# x, y, z = int(input("Введите первое число: ")), int(input("Введите второе число: ")), int(input("Введите третье число: "))
#
# def my_func(a, b, c):
#
#     if a > c and b > c:
#         return a + b
#     elif c > a and a > b:
#         return a + c
#     else:
#         return b + c
#
# print(f"Полученный езультат суммы двух наибольших чисел: {my_func(x, y, z)}")

# №4

# x, y = int(input("Введите число: ")) , int(input("Введите число: "))
#
# def my_func(x, y):
#     try:
#         if x >= 0 and y <= 0:
#             return x**y
#     except SyntaxError:
#         print("Введено неверное значение! Вторая переменная - отрицательная!")
#
# print(f"Полученный результат: {my_func(x,y)}")
# ____________________________________________________________________________________________________

# def my_func(*args):
#     x, y = int(input("Введите число: ")), int(input("Введите число: "))
#     try:
#         if x >= 0 and y <= 0:
#             return pow(x,y)
#     except SyntaxError:
#         print("Введено неверное значение! Вторая переменная - отрицательная!")
#
# print(f"Полученный результат: {my_func()}")

# №5
#
# def my_func ():
#     result = 0
#
#     while result != "gg":
#         number = input("Введите числа через пробел: ").split()
#         for i in range(len(number)):
#             if number[i] != int() and number == "gg":
#                 break
#             else:
#                 result = result + int(number[i])
#         print(f"Сумма элементов равна: {result}")
#     print(f"Финальная сумма: {result}")
#
# my_func()

# №6 / №7

# def int_func(str):
#     return str[0].upper() + str[1:].lower()
#
# print(int_func(str(input("Введите данные: "))))


# def int_func(*args):
#     text = input("Введите слова: ")
#     return print(text.title())
# int_func()
