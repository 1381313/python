import turtle as t
import random
a=3000
cx=[0.0,1.0,0.5]
cy=[0.0,0.0,0.866]
x,y=0,0
for i in range(a):
    r=random.randrange(0,3)
    x= (x+cx[r])/2.0
    y= (y+cy[r])/2.0
    t.penup()
    t.goto(200*x,200*y)
    t.dot(5,'red')

t.done()
