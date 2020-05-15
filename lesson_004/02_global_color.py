# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

import simple_draw as sd

sd.resolution = (1200, 600)
color_dict = {0:'COLOR_RED', 1:'COLOR_ORANGE', 2:'COLOR_YELLOW',
              3:'COLOR_GREEN', 4:'COLOR_CYAN', 5:'COLOR_BLUE', 6:'COLOR_PURPLE'}


def fig(point, length, angle, angle1):
    for i, name in color_dict.items():
        print(i, name)
    color = int(input("Выбери из цвет списка  "))

    for angle in range(angle, angle + 359, angle1):
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
        c1=color_dict[color]
        print(c1)
        v1.draw(color=sd.c1)
        point=v1.end_point

def treeangle(point = sd.get_point(300, 300), length = 100, angle = 0):
    fig(point=point, length=length, angle=angle, angle1=120)
    l1=sd.line(point,point)


# - квадрата
def quadro(point = sd.get_point(300, 300), length = 100, angle = 0):
    fig(point=point, length=length, angle=angle, angle1=90)

# # - пятиугольника
def fangle(point = sd.get_point(100, 300), length = 100, angle = 0):
    fig(point=point, length=length, angle=angle, angle1=72)

# # - шестиугольника

def sangle(point = sd.get_point(300, 300), length = 100, angle = 0):
    fig(point=point, length=length, angle=angle, angle1=60)

treeangle(point = sd.get_point(100, 100), length = 500, angle = 30)
# quadro(point = sd.get_point(400, 100), length = 200, angle = 45)
# fangle(point = sd.get_point(600, 50), length = 100, angle = 0)
# sangle(point = sd.get_point(200, 300), length = 100, angle = 0)

sd.pause()
