import random # Випадкове будь шо
import turtle # Черепашка шо малює

t = turtle.Turtle() # екземпляр черепашки
wn = turtle.Screen() # Вікно

t.speed(10) # Швидкість малювання

wn.bgcolor("black") # Колір фону
t.color("white") # Колір лінії
turtle.colormode(255) # Діапазон кольорової схеми RGB

def leaf():
    t.forward(5) # Вперед на 5 пікселів
    t.right(60) # повертаємо вправо на 60°
    t.circle(30,60) # креслимо дугу радіусом 30 пікселів на 60°
    t.right(-120)
    t.circle(30,60)
    t.right(180)
    t.forward(10)

def randNum():
    a = random.randint(1000, 100000)
    count = 0 # Лічильник листочків
    color_mod = 0

    while a > 1 and count < 40:
        count += 1
        color_mod +=5
        # Поступова зміна кольору
        t.color(0, count * 2, 100 - count)
        # Алгоритм Коллатца
        if a % 2 == 0: # Чи парне число
            a = a / 2
            leaf()
            t.right(10)
        else:
            a = a * 3 + 1
            leaf()
            t.left(20)

for i in range(10000):
    wn.tracer(0) 

    t.penup() # Піднімає пензль, щоб переміщувати без малювання
    t.goto(0, -300) # Переміщує по "x" та "y"
    t.setheading(90) # Повертає вгору
    t.pendown() # Опускає пензль

    randNum() # Малює листочок

    wn.tracer(1) # 



turtle.exitonclick() # Чекати на клік для закриття вікна