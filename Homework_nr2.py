# №1
# spisok = [31, 98.9, "земля", ("солнце", 56, 334.9)]
# print(spisok)
# for a in spisok:
#     print(type(a))

# №2

# a = int(input("Введите кол-во элементов: "))
# spisok = []
# b = 0
# c = 0
# while b < a:
#     spisok.append(input("Введите значение списка: "))
#     b += 1
# for d in range(int(len(spisok)/2)):
#         spisok[c], spisok[c + 1] = spisok[c + 1], spisok[c]
#         c += 2
# print(spisok)

# №3

# x = int(input("Введите месяц в числовом формате "))
#
# month = {"Январь": 1, "Февраль": 2, "Март": 3, "Апрель": 4, "Май": 5, "Июнь": 6, "Июль": 7, "Август": 8, "Сентябрь": 9, "Октябрь": 10, "Ноябрь": 11, "Декабрь": 12}
# season = {"Зима": ["Декабрь", "Январь", "Февраль"], "Весна": ["Март", "Апрель", "Май"], "Лето": ["Июнь", "Июль", "Август"], "Осень": ["Сентябрь", "Октябрь", "Ноябрь"]}
# season_dict = {1: "Зима", 2: "Весна", 3: "Лето", 4: "Осень"}
#
# if x == 1 or x == 2 or x == 12:
#     print(season_dict.get(1)
# elif x == 3 or x == 4 or x == 5:
#     print(season_dict.get(2)
# elif x == 6 or x == 7 or x == 8:
#     print(season_dict.get(3)
# elif x == 9 or x == 10 or x == 11:
#     print(season_dict.get(4)
# else:
#     print("В году только 12 месяцев")

# №4

# x = input("Введите несколько слов ")
#
# spisok = []
# nr = 1
#
# for a in range(x.count(" ") + 1):
#     spisok = x.split()
#     if len(str(spisok)) <= 10:
#         print(f" #{nr} {spisok[a]}")
#         nr += 1
#     else:
#         print(f" #{nr} {spisok[a][0:10]}")
#         nr += 1

# №5

# my_list = [7, 5, 3, 3, 2]
# print(f"Рейтинг: {my_list}")
#
# x = int(input("Введите число: "))
# while x:
#     for i in range(len(my_list)):
#         if my_list[i] == x:
#             my_list.insert(i + 1, x)
#             break
#         elif my_list[0] < x:
#             my_list.insert(0, x)
#             break
#         elif my_list[-1] > x:
#             my_list.append(x)
#             break
#         print(f"Новый список: {my_list}")
#         x = int(input("Введите число: "))

# №6

# goods = {"название": ["компьютер", "принтер", "сканер"]}
# price = {"цена": [20000, 6000, 2000]}
# quantity = {"количество": [5, 2, 7]}
# value ={"ед": "шт."}
# info = ["компьютер", "принтер", "сканер"]
#
# a = int(input("Выбирите нужный товар, где 1 - компьютер, 2 - принтер, 3 - сканер: "))
#
# for i in range(len(info)):
#
#     if a == 1:
#         price.keys() and price.get(0)
#         quantity.keys() and quantity.get(0)
#         value.items()
#
#     elif a == 2:
#         price.keys() and price.get(1)
#         quantity.keys() and quantity.get(1)
#         value.items()
#
#     elif a == 3:
#         price.keys() and price.get(2)
#         quantity.keys() and quantity.get(2)
#         value.items()
#
# print(f"Подробная информация о товаре: {a}")
