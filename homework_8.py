# №1

# class Date():
#
#     def __init__(self, day_month_year):
#         self.day_month_year = str(day_month_year)
#
#
#     def __str__(self):
#         return f"Текущая дата: {Date.numb(self.day_month_year)}"
#
#     @classmethod
#
#     def numb(cls, day_month_year):
#         date_nb = []
#
#         for i in day_month_year.split():
#             if i != '': date_nb.append(i)
#
#         return int(date_nb[0]), int(date_nb[1]), int(date_nb[2])
#
#     @staticmethod
#
#     def number_of_date(day, month, year):
#
#         if 1 <= day <= 31:
#             if 1 <= month <= 12:
#                 if 2022 >= year >= 0:
#                     return f'Все верно!'
#                 else:
#                     return f'Неправильный год!'
#             else:
#                 return f'Неправильный месяц!'
#         else:
#             return f'Неправильный день!'
#
#
# d = Date('30 8 2022')
# print(f'Сегодня {d}')
# print(Date.number_of_date(1, 8, 2022))
# print(Date.number_of_date(29, 8, 2023))
# print(Date.number_of_date(29, 13, 2022))
# print(d.number_of_date(31,12,2021))
# print(Date.numb("29 8 2022"))
# print(d.numb("10 12 1991"))

# №2
#
# class Error(Exception):
#     def __init__(self, divisible, divisor):
#         self.divisible = divisible
#         self.divisor = divisor
#
#     @staticmethod
#
#     def Null_Error(divisible, divisor):
#         try:
#             return (divisible / divisor)
#
#         except:
#             return (f'На ноль делить нельзя!')
#
# a = Error(30,0)
#
# print(Error.Null_Error(100,0))
# print(Error.Null_Error(10,5))
# print(a.Null_Error(30,0))


# №3

# import traceback
# class CastomError(Exception):
#
#     def __init__(self, *args):
#         self.my_list = []
#         print("Если желаете остановиться, введите слово Stop")
#         while True:
#             inp_data = input('Введите значение: ')
#             try:
#                 self.my_list.append(int(inp_data))
#             except ValueError as err:
#                 if inp_data == "Stop" or inp_data == "stop":
#                     break
#                 print(f'Введено неверное значение!', traceback.format_exc())
#
#
#     def __str__(self):
#         return ','.join(map(str, self.my_list))
#
#
# a = CastomError()
# print(a)

# №4/№5/№6

# class Equipment():
#
#     def __init__(self, name, price, quantity, numb, *args):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#         self.numb = numb
#         self.warehouse = []
#         self.my_dict = {'Модель': self.name, 'Цена за единицу': self.price, 'Кол-во': self.quantity}
#
#     def __str__(self):
#         return f'Модель {self.name} цена {self.price} в кол-ве {self.quantity} единиц/ы.'
#
#     def acceptance(self):
#         try:
#             pos_1 = input('Введите классификацию товара: ')
#             pos_2 = int(input('Введите цену за единицу товара: '))
#             pos_3 = int(input('Введите необходимое кол-во товара: '))
#             pos_dict = {'Модель': pos_1, 'Цена за единицу': pos_2, 'Кол-во':pos_3}
#             self.my_dict.update(pos_dict)
#             self.warehouse.append(self.my_dict)
#             print(f'Выбранные элементы: {self.warehouse}')
#         except:
#             return f'Неверные данные.'
#
#         print('Нажмите Enter для продолжения. Если желаете остановиться, введите слово Stop')
#         stop = input(" ")
#         if stop == "Stop" or pos_1 == "stop":
#             return f'Завершение'
#         else:
#             return Equipment.acceptance(self)
#
# class Printer(Equipment):
#     def to_print(self):
#         return f'Распечатать {self.numb} раз'
#
# class Scanner(Equipment):
#     def to_scan(self):
#         return f'Отсканировать {self.numb} раз'
#
# class Copier(Equipment):
#     def to_copie(self):
#         return f'Сделать копию {self.numb} раз'
#
# p = Printer('Canon', 12000, 5, 100)
# s = Scanner('Epson', 7500, 3, 55)
# c = Copier('HP', 4400, 4, 30)
#
#
# print(p.acceptance())
# print(s.acceptance())
# print(c.acceptance())
#
# print(p)
# print(p.to_print())
#
# print(s)
# print(s.to_scan())
#
# print(c)
# print(c.to_copie())

# №7

# class ComplexNmb():
#     def __init__(self, ac, im):
#         self.ac = ac
#         self.im = im
#
#     def __add__(self, other):
#         return f'Сумма двух комплексных чисел составляет: {other.ac + self.ac} + {other.im + self.im} * i'
#
#     def __mul__(self, other):
#         return f'Произведение двух комплексных чисел составляет: {other.ac * self.ac - other.im * self.im} + {self.im * other.ac + self.ac * other.im} * i'
#
#     def __str__(self):
#         return f'Вывод комплексных значений: {self.ac} , {self.im} * i'
#
# ac = float(input('Введите число: '))
# im = float(input('Введите второе число: '))
# first = ComplexNmb(ac,im)
# second = ComplexNmb(ac,im)
#
# print(first + second)
# print(first * second)
# print(first)
