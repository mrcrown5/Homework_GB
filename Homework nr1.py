# №1
# a = 11
# b = 25
# print(b-a)
# print(a*a-b)
#
# a = (a**2 - 1 + b)
# print(a)
#
# year = "2022"
# print(year)
# print(type(year))
#
# name = input("Как тебя зовут?")
# print(f"Привет, {name}!")
#
# age = int(input("Сколько тебе лет?"))
# print(f"{age} Ого, как быстро ты вырос!")

# №2
# time = int(input("Время в секундах: "))
# h = time / 3600
# round(h,3)
# m = (time - h) / 60
# round(m,3)
# s = time
# print (f"Точное время чч:мм:сс {round(h,4)}: {round(m,4)}: {s}")

# №3
# n = int(input("Введите любое однозначное число "))
# nn = str(n) + str(n)
# nnn = str(n)+ str(n) + str(n)
# s = int(n) + int(nn) + int(nnn)
# print(f"Сумма чисел: {n} + {nn} + {nnn} = {s}")

# №4
# a = abs(int(input("Введите целое положительное число ")))
# while a >=1:
#   if a <= 0:
#       break
# print(f"Самая большая цифра - {a}")

# №5 / №6
# income = float(input("Выручка фирмы: "))
# costs = float(input("Издержки фирмы: "))
#
# if income > costs:
#     print(f"Фирма работает успешно и рентабельность составила: {round(income / costs,2)}")
#     employees = int(input("Кол-во работников на предприятии: "))
#     print(f"Прибыль каждого работника составила {round(income / employees),1}")
# elif income == costs:
#     print("Фирма работает в ноль")
# else:
#     print("Фирма на грани банкротства")

# №7
# a = int(input("Пройденные км за день "))
# b = int(input("Ожидаемое кол_во км за день "))
# day = 1
# while a < b:
#     a = a + a * 0.1
#     day = day + 1
#     break
# print(f"День, когда спортсмен достиг желаемого результата {day}")
