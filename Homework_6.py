# №1

# import time
# class TrafficLight ():
#
#     color = ["Красный", "Желтый", "Зеленый"]
#     def running(self):
#         """Изменение цвета светофора"""
#         i = 0
#         while i < 3:
#             print(f"Переключение сигнала светофора на {TrafficLight.color[i]}")
#             if i == 0:
#                 time.sleep(7)
#             elif i == 1:
#                 time.sleep(2)
#             elif i == 2:
#                 time.sleep(10)
#             i += 1
#
# Svetafor = TrafficLight()
# Svetafor.running()

# №2
#
# class Road ():
#     """вес одного 1 квадратного метра толщиной в 1 см"""
#     thick = 25
#     def __init__(self, lengh, width):
#
#         self._lengh = lengh
#         self._width = width
#
#     def mass(self, depth):
#         return self._lengh * self._width * self.thick * depth
#
# Trassa1 = Road(20,5000)
# print(f"Необходимая масса асвальтового покрытия составляет {Trassa1.mass(5)/1000} тонн")

# №3

# class Worker():
#
#     def __init__(self, name, surname, position, wage, bonus):
#
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = {"wage": wage, "bonus": bonus}
#
#
# class Position(Worker):
#
#     def __init__(self, name, surname, position, wage, bonus):
#         super().__init__(name, surname, position, wage, bonus)
#
#     def full_name(self):
#         return self.name + " " + self.surname
#
#     def total_income(self):
#         return self._income.get("wage") + self._income.get("bonus")
#
# person_1 = Position("Alex", "Smirnov", "General_manager", 33000, 10000)
# person_2 = Position("Leo", "Antipov", "PR_manager", 27000, 5000)
# person_3 = Position("Sofia", "Morizova", "Accountant", 25000, 4000)
#
#
# print(f"{person_1.full_name()} с сумарным доходом {person_1.total_income()}")
# print(f"{person_2.full_name()} с сумарным доходом {person_2.total_income()}")
# print(f"{person_3.full_name()} с сумарным доходом {person_3.total_income()}")

# №4
#
# class Car():
#
#     def __init__(self, speed, color, name, is_police):
#
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#
#     def go(self):
#         return("Машина начала движение")
#
#     def stop(self):
#         return("Машина остановилась")
#
#     def turn_right(self):
#         return("Машина изменила траекторию и повернула направо")
#
#     def turn_left(self):
#         return("Машина изменила траекторию и повернула налево")
#
#     def show_speed(self):
#         return("Скорость автомобиля")
#
# class TownCar(Car):
#     def __init__(self, speed, color, name, is_police):
#         super().__init__(speed, color, name, is_police)
#
#     def show_speed(self):
#         if self.speed > 60:
#             return ("Автомобиль превышает скорость!")
#         else:
#             return("Скорость автомобиля в допустимом диапазоне.")
#
# class SportCar(Car):
#     def __init__(self, speed, color, name, is_police):
#         super().__init__(speed, color, name, is_police)
#
# class WorkCar(Car):
#     def __init__(self, speed, color, name, is_police):
#         super().__init__(speed, color, name, is_police)
#
#     def show_speed(self):
#         if self.speed > 40:
#             return("Превышение скорость!")
#         else:
#             return("Скорость автомобиля в допустимом диапазоне.")
#
# class PoliceCar(Car):
#     def __init__(self, speed, color, name, is_police):
#         super().__init__(speed, color, name, is_police)
#
#     def police(self):
#         if self.is_police == True:
#             return("Причастен к ГИБДД")
#         else:
#             return("Автомобиль не причастен к ГИБДД")
#
# auto_1 = Car(130, "Красный", "Mercedes-Benz", False)
# auto_2 = TownCar(90, "Черный", "Audi", False)
# auto_3 = SportCar(220, "Желтый", "Lamborghini", False)
# auto_4 = WorkCar(35, "Серый", "Volkswagen", False)
# auto_5 = PoliceCar(50, "Бело-синий", "Lada", True)
#
# print(f"{auto_1.color} {auto_1.name}, {auto_1.stop()} около заправки, хотя скорость на трассе была около {auto_1.speed} км/ч")
# print(f"А вот {auto_3.color} {auto_3.name} не успел среагировать и поймал камеру при скорости {auto_3.speed} км/ч. Поэтому полицеский {auto_5.is_police} авто выехал на перехват на {auto_5.color} {auto_5.name}, который {auto_5.police()}.")
# print(f"{auto_2.color} {auto_2.name} {auto_2.go()}, но всткоре {auto_2.turn_left()} и получила штраф. Скорость {auto_2.speed} была недопустимой! {auto_2.show_speed()}")
# print(f"И только {auto_4.color} {auto_4.name} передвигался с положенной скоростью {auto_4.speed}, тем самым выдавая себя за полицескую машину {auto_4.is_police}, что было не так.")

# №5
#
# class Stationery():
#
#     def __init__(self, title):
#         self.title = title
#
#     def draw(self):
#         return("Запуск отрисовки")
#
# class Pen(Stationery):
#     def __init__(self, title):
#         super().__init__(title)
#     def draw(self):
#         return("Тонкость пера")
#
# class Pencil(Stationery):
#     def __init__(self, title):
#         super().__init__(title)
#     def draw(self):
#         return("Возможность редактировать")
#
# class Handle(Stationery):
#     def __init__(self, title):
#         super().__init__(title)
#     def draw(self):
#         return("Выделение важного")
#
# instance_1 = Stationery("Кисть")
# instance_2 = Pen("Ручка")
# instance_3 = Pencil("Карандаш")
# instance_4 = Handle("Маркер")
#
# print(f"Легким движением руки {instance_1.title} производит {instance_1.draw()}.")
# print(f"Не смотря на то, что {instance_2.title} имеет {instance_2.draw()}, большинство художников предпочитают {instance_3.draw()}, которая есть только у {instance_3.title}.")
# print(f"Однако, иметь возможность не закрасить все, а произвести {instance_4.draw()} может поспособствовать только {instance_4.title}. Один из необходимых инструментов как в учебе, так и в работе.")
