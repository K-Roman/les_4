# -*- coding: utf-8 -*-

import simple_draw as sd


sd.resolution = (1200, 600)

point_0 = sd.get_point(600, 0)

def branch(point, angle, length):
    if length < 5:
        return
    v1 = sd.get_vector(start_point=point, angle=angle+30, length=length, width=3)
    v1.draw()
    v2 = sd.get_vector(start_point=point, angle=angle-30, length=length, width=3)
    v2.draw()
    next_point1 = v1.end_point
    next_point2 = v2.end_point
    a = sd.random_number(-40,40)/100
    b = sd.random_number(80,120)/100
    next_angle1 = angle + 30 + (30*a)
    next_angle2 = angle - 30 + (30*a)
    next_length = length*0.75*b
    branch(point=next_point1, angle=next_angle1, length=next_length)
    branch(point=next_point2, angle=next_angle2, length=next_length)
branch(point=point_0, angle=90, length=100)
# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# TODO здесь ваш код

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()


