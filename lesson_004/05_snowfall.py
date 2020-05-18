# -*- coding: utf-8 -*-

import simple_draw as sd
import random

n=0
list_x=[]
list_y=[]
list_l=[]
while n<100:
    list_x.append(random.randint(50,1100))
    list_y.append(random.randint(250,600))
    list_l.append(random.randint(10, 25))
    n = n + 1
sd.resolution = (1200, 600)

print(len(list_x))
# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные



# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

# TODO здесь ваш код


# for i in list_x:
#     y = random.choice(list_y)
#     x = random.choice(list_x)
#     length = sd.random_number(10, 101

for i, item in enumerate(list_x):
    x = list_x[i]
    y = list_y[i]
    point_0 = sd.get_point(x, y)
    length = list_l[i]
    sd.snowflake(center=point_0, length=length)

while True:
    for i, item in enumerate(list_y):
        a = sd.random_number(-25, 25)
        x = list_x[i] + a
        y = list_y[i] - 10
        point_0 = sd.get_point(x, y)
        length = list_l[i]
        sd.snowflake(center=point_0, length=length)
        list_y[i]=list_y[i] - 10
        if y < 20:
            list_y[i]=random.choice(list_y)

    sd.sleep(0.2)
    sd.clear_screen()





sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


