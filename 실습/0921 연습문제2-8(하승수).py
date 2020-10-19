import turtle
import random

## 함수 선언 부분 ##

def  screenLeftClick(x,y):
    tSize = random.randrange(2,10) #거북이크기

    r = random.random() #red, green, blue 색상지정
    g = random.random()
    b = random.random()  

    
    tAngle = random.randrange(0, 360) #회전 각도

    turtle.penup()
    turtle.goto(x,y)

    turtle.color(r,g,b)
    turtle.shapesize(tSize)
    turtle.left(tAngle) 
    turtle.stamp() # 거북이 복제


## 변수 선언 부분 ##
tSize, tAngle = 0, 0
r, g, b = 0.0, 0.0, 0.0

## 메인 코드 부분 ##
turtle.title('거북이 도장 찍기')
turtle.shape('turtle')

turtle.onscreenclick(screenLeftClick,1)

turtle.done()
