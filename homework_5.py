# №1
#
# f = open("hello.txt", "w")
# f.write("Hello,world! \n")
# f.write("I'm glad to see u here \n")
# f.close()
#
# f = open("hello.txt", "r")
# print(f.read())
# # print(f.readlines())
# # print(f.readline())
# f.close()

# №2
#
# '''Первое условие по подсчету слов и элементов'''
#
# f = open("test_file.txt", "r")
# y = f.read()
# print(f"Кол-во элементов в файле составляет: {len(y)}")
# print(f"Кол-во слов в файле составляет: {len(y.split())}")
# f.close()
#
# '''Второе условие по подсчету строк (работает при закомментированной первой части)'''
# with open("test_file.txt", "r") as f:
#     print(f"Кол-во строк в файле составляет: {len(f.readlines())}")

# №3

# people = 0
# summ = 0
# with open("firma.txt", "r+") as f:
#     for i in f.readlines():
#         people += 1
#         summ += float(i.split()[1])
#         if float(i.split()[1]) < 20000:
#             print(i.split()[0])
#
# print(f"Средний доход равен = {round((summ/people),2)}")

# №4

# nmb = {"One":"Один", "Two":"Два", "Three":"Три", "Four":"Четыре"}
# n = open("numbers.txt", "r", encoding="utf-8")
# x = open("nmbrs2.txt", "a", encoding="utf-8")
# for i in n.readlines():
#     for el in nmb:
#         if el == i.split()[0]:
#             i = i.replace(i.split()[0], nmb.get(el))
#             x.write(f"{i}")
#             print(i)
#
# n.close()
# x.close()


# №5

# """Программно - созданный текствой файл"""
# with open("nmb.txt", "w", encoding="utf-8") as n:
#     n.write("1 2 3 4 5\n")
#
# import re
#
# summation = open("nmb.txt", "r+", encoding="utf-8")
# summ = 0
#
# s = summation.read()
# s = re.findall(r"[+-]?\d+", s)
# s = [int(i) for i in s]
#
# for i in s:
#     summ += i
#
# summation.write(str(summ))
# summation.close()
#
# """Для вывода суммы введенных чисел"""
# with open("nmb.txt", "r", encoding="utf-8") as S:
#     SM = S.readlines()[1]
#     print(f"Сумма введенных чисел равна = {SM}")

# №6

# import re
# dictionary = {}
# with open("study.txt", "r+", encoding="utf-8") as s:
#
#     for line in s.readlines():
#         lesson = line.split()[0]
#         zaniatija = 0
#
#         for i in re.findall("\d+", line):
#             zaniatija += int(i)
#         dictionary.update({lesson: zaniatija})
#
# print(dictionary)

# №7
# import re
# import json
#
# income = {}
# average_pfofit = {}
# with open("firms.txt", "r+", encoding="utf-8") as f:
#     for line in f.readlines():
#         firms = line.split()[0]
#         money = 0
#
#         for i in re.findall("\d+", line):
#             money += int(i)
#         income.update({firms: money})
# print(income)
#
# with open("firms.txt", "w", encoding="utf-8") as j:
#     json.dump(income, j)
#     json_str = json.dumps(income)
#     print(json_str)
