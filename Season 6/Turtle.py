
import turtle

p = turtle.Pen("turtle")
p.width(1)
p.color("red")



def trtle():
    a = 30
    b = 10

    for j in range(3, 20):
        x = ((j - 2) * 180) / j
        p.left(180 - (x / 2))

        for i in range (j):
            p.forward(a)
            p.left(180 - x)
        p.right(180 - (x / 2))
        p.penup()
        p.forward(b)
        p.pendown()

        a += 10
        b += 2
    
trtle()
turtle.done()

