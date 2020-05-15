# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника

def fig(point, length, angle, angle1):
    for angle in range(angle, angle + 359, angle1):
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
        v1.draw()
        point=v1.end_point

def treeangle(point = sd.get_point(300, 300), length = 100, angle = 0):
    fig(point=point, length=length, angle=angle, angle1=120)
    l1=sd.line(point,point)

#     for angle in range(angle, angle + 361, 120):
#         v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#         v1.draw()
#         point=v1.end_point
# treeangle(point = sd.get_point(100, 100), length = 200, angle = 30)

# - квадрата
def quadro(point = sd.get_point(300, 300), length = 100, angle = 0):
    fig(point=point, length=length, angle=angle, angle1=90)
#     angle_1 = 90
#     fig(point=point, length=100, angle=0, angle_1=angle_1)
# #     for angle in range(angle, angle + 361, 90):
# #         v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
# #         v1.draw()
# #         point=v1.end_point
# # quadro(point = sd.get_point(400, 100), length = 200, angle = 45)
#
#
# # - пятиугольника
def fangle(point = sd.get_point(100, 300), length = 100, angle = 0):
    fig(point=point, length=length, angle=angle, angle1=72)
#     angle_1 = 72
#     fig(point=point, length=100, angle=0, angle_1=angle_1)
#     # for angle in range(angle, angle + 361, 72):
# #         v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
# #         v1.draw()
# #         point=v1.end_point
# # fangle(point = sd.get_point(600, 50), length = 100, angle = 0)
#
#
# # - шестиугольника
#
def sangle(point = sd.get_point(300, 300), length = 100, angle = 0):
    fig(point=point, length=length, angle=angle, angle1=60)
#     angle_1 = 60
#     fig(point=point, length = 100, angle  = 0, angle_1=angle_1)
#     # for angle in range(angle, angle + 361, 60):
#     #     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     #     v1.draw()
#     #     point=v1.end_point
# sangle(point = sd.get_point(200, 300), length = 100, angle = 0)

treeangle(point = sd.get_point(100, 100), length = 500, angle = 30)
quadro(point = sd.get_point(400, 100), length = 200, angle = 45)
fangle(point = sd.get_point(600, 50), length = 100, angle = 0)
sangle(point = sd.get_point(200, 300), length = 100, angle = 0)


# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# TODO здесь ваш код

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
