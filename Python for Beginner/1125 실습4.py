import turtle
import random
import math
from tkinter.simpledialog import *

swidth,sheight = 300,300

turtle.title("거북이 글자쓰기")
turtle.shape("turtle")
turtle.setup(width=swidth + 50, height=sheight+50)
turtle.screensize(swidth,sheight)
turtle.penup()
angle = 0


inStr = askstring('문자열 입력','거북이 쓸 문자열을 입력')
div_ang = 360/len(inStr)

for ch in inStr:
    tX = 100 * math.cos(3.14*angle/180)
    tY = 100 * math.sin(3.14*angle/180)
    angle = angle + div_ang
    #angle += div_ang
    #tX = random.randrange(-swidth/2,swidth/2)
    #tY = random.randrange(-sheight/2,sheight/2)
    r=random.random(); g=random.random(); b=random.random();
    #txtSize = random.randrange(10,50)
    txtSize=20

    turtle.goto(tX,tY)

    turtle.pencolor(r,g,b)
    turtle.write(ch,font=('맑은 고딕',txtSize,'bold'))

turtle.done()
    
