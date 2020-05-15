# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg


sd.resolution = (1200, 600)

form_dict = {0:'треугольник', 1:'квадрат', 2:'пятиугольник',
              3:'шестиугольник'}

def fig(point, length, angle):
    for i, name in form_dict.items():
        print(i, name)
    shape = int(input('введите желаемую форму   '))
    angles = {0:120, 1:90, 2:72, 3:60}
    print(int(angles[shape]))
    for angle in range(angle, angle + 359, angles[shape]):
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
        v1.draw()
        point=v1.end_point

fig(point = sd.get_point(100, 100), length = 500, angle = 30)




sd.pause()
