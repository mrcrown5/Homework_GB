# №1

# class Matrix():
#
#     def __init__(self, list_1):
#         self.list_1 = list_1
#
#     def __str__(self):
#         for a in self.list_1:
#             for b in a:
#                 print(f"{b:3}", end="")
#             print()
#         return ""
#
#     def __add__(self, list_2):
#         for i in range(len(self.list_1)):
#             for j in range(len(list_2.list_1[i])):
#                 self.list_1[i][j] = self.list_1[i][j] + list_2.list_1[i][j]
#
#         return Matrix.__str__(self)
#
#
# x = Matrix([[1,2,3], [4,5,6], [7,8,9]])
# y = Matrix([[11,12,13], [14,15,16], [17,18,19]])
#
# print(x + y)

# №2

# class Clothes():
#
#     def __init__(self, name, size, height):
#         self.name = name
#         self.size = size
#         self.height = height
#
#     def count_size(self):
#         return self.size / 6.5 + 0.5
#
#     def count_height(self):
#         return self.height * 2 + 0.3
#
#     @property
#     def count_sum(self):
#         return str(f"Сумарный объем ткани составляет {round((self.size / 6.5 + 0.5),2) + round((self.height * 2 + 0.3),2)}")
#
# class Coat(Clothes):
#     def __init__(self, name, size, height):
#         super().__init__(name, size, height)
#
#     def __str__(self):
#         return (f"Объем ткани на пальто {round((self.size / 6.5 + 0.5),2)}")
#
#
# class Suit(Clothes):
#     def __init__(self, name, size, height):
#         super().__init__(name, size, height)
#
#     def __str__(self):
#         return (f"Объем ткани на костюм {round((self.height * 2 + 0.3),2)}")
#
#
# c = Coat("Пальто H&M", 42, 176)
# s = Suit("Костюм Dolce&Gabbana", 46, 191)
#
# print(c)
# print(s)
#
# print(f"Для {c.name}, {c.count_sum}")
# print(f"Для {s.name}, {s.count_sum}")
#

# №3

# class Cell():
#
#     def __init__(self, value):
#         self.value = int(value)
#
#     def __add__(self, other):
#         return Cell(int(self.value + other.value))
#
#     def __sub__(self, other):
#         return Cell(self.value - other.value if self.value - other.value > 0 else print("Разность должна быть больше нуля!"))
#
#     def __mul__(self, other):
#         return Cell(int(self.value * other.value))
#
#     def __truediv__(self, other):
#         return Cell(int(round(self.value) / round(other.value)))
#
#     def __str__(self):
#         return (f'Вывод результатов {self.value * "x"}')
#
#     def make_order(self, value_row):
#         row = "x"
#         for i in range(int(self.value / value_row)):
#             row += f'{"x" * value_row} \\n'
#         row += f'{"x" * (self.value % value_row)}'
#         return row
#
# c_1 = Cell(46)
# c_2 = Cell(5)
#
# print(c_1)
# print(c_1 + c_2)
# print(c_1 - c_2)
# print(c_1 * c_2)
# print(c_1 / c_2)
# print(c_1.make_order(12))
# print(c_2.make_order(2))
