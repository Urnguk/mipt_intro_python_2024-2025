import turtle

# turtle.speed(0)
# turtle.color("red")
# full_angle = 360
# R = 100
# L = 2 * 3.14 * R
# k = 100
# d = L / k
# turtle.penup()
# turtle.goto(-300, 300)
# turtle.pendown()
# while True:
#     turtle.fd(d)
#     turtle.rt(full_angle / k)
# turtle.circle(100)
# turtle.done()



# T1 = turtle.Turtle()
# T2 = turtle.Turtle()
# T1.width(10)
# T1.color("#00a9a6")
# T2.color("#3c3c3d")
# T1.goto(0, 200)
# T2.goto(0, 200)
# while True:
#     T1.fd(10)
#     T1.right(5)
#     T2.fd(15)
#     T2.rt(2.5)
#
# turtle.done()


# def coh_line(n, d):
#     if n == 0:
#         turtle.fd(d)
#         return
#     coh_line(n - 1, d // 3)
#     turtle.left(60)
#     coh_line(n - 1, d // 3)
#     turtle.right(120)
#     coh_line(n - 1, d // 3)
#     turtle.left(60)
#     coh_line(n - 1, d // 3)
#
#
# turtle.tracer(0)
# turtle.speed(0)
# turtle.pu()
# turtle.goto(-500, 200)
# turtle.pd()
# coh_line(6, 800)
# turtle.right(120)
# coh_line(6, 800)
# turtle.right(120)
# coh_line(6, 800)
# turtle.update()
# turtle.done()

# import turtle
# t1 = turtle.Turtle()
# t2 = turtle.Turtle()
# t3 = turtle.Turtle()
# t4 = turtle.Turtle()
# t5 = turtle.Turtle()
# t6 = turtle.Turtle()
# t7 = turtle.Turtle()
# t1.color('red')
# t2.color('orange')
# t3.color('yellow')
# t4.color('green')
# t5.color('light blue')
# t6.color('blue')
# t7.color('purple')
# def rainbow(t, i):
#     t.penup()
#     t.goto(-100+5*i, 0)
#     t.lt(90)
#     t.pendown()
#     t.circle(50, 180)
# rainbow(t1, 1)
# rainbow(t2, 2)
# rainbow(t3, 3)
# rainbow(t4, 4)
# rainbow(t5, 5)
# rainbow(t6, 6)
# rainbow(t7, 7)
#
# turtle.done()

# def levi_curve(n, d):
#     if n == 0:
#         turtle.forward(d)
#         return
#     turtle.left(45)
#     levi_curve(n - 1, d * (2 ** (-0.5)))
#     turtle.right(90)
#     levi_curve(n - 1, d * (2 ** (-0.5)))
#     turtle.left(45)
#
# def minkovskiy_curve(n, d):
#     if n == 0:
#         turtle.forward(d)
#         return
#     minkovskiy_curve(n - 1, d // 4)
#     turtle.left(90)
#     minkovskiy_curve(n - 1, d // 4)
#     turtle.right(90)
#     minkovskiy_curve(n - 1, d // 4)
#     turtle.right(90)
#     minkovskiy_curve(n - 1, d // 4)
#     minkovskiy_curve(n - 1, d // 4)
#     turtle.left(90)
#     minkovskiy_curve(n - 1, d // 4)
#     turtle.left(90)
#     minkovskiy_curve(n - 1, d // 4)
#     turtle.right(90)
#     minkovskiy_curve(n - 1, d // 4)
#
#
# turtle.tracer(0)
# turtle.pu()
# turtle.goto(-300, 100)
# turtle.pd()
# for i in range(4):
#     minkovskiy_curve(3, 256)
#     turtle.right(90)
# turtle.update()
# turtle.done()

turtle.tracer(0)

n = 8
d = 10
seq = []
for i in range(n):
    seq = seq + [True] + [not(x) for x in seq[::-1]]

turtle.fd(d)
for i in range(len(seq)):
    if seq[i]:
        turtle.right(90)
    else:
        turtle.left(90)
    turtle.fd(d)
turtle.update()
turtle.done()

