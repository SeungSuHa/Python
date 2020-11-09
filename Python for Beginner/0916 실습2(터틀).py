#모듈 선언
import turtle
import random

'''함수 선언
def로 함수를 만들 수 있다
함수이름은 단어의 첫 글자를 대문자로 사용해 강조한다'''

def screenLeftClick(x,y):

        #global:전체에서 다 쓰겠다
        global r,g,b
        turtle.pencolor(r,g,b)
        #pendown 선 그리기
        turtle.pendown()
        #goto 좌표 x,y로 가겠다
        turtle.goto(x,y)

def screenRightClick(x,y):
        #penup 선 안 그리기
        turtle.penup()
        turtle.goto(x,y)

def screenMidClick(x,y):
        global r,g,b
        #tSize 거북이의 크기 random으로 1부터 10까지 범위
        tSize = random.randrange(1,10)
        #pSize 펜의 굵기 random으로 5부터 25까지 범위
        pSize = random.randrange(5,25)
        turtle.pensize(pSize)
        turtle.shapesize(tSize)
        r=random.random()
        g=random.random()
        b=random.random()
        
#변수 선언


#r=0.0 b=0.0 c=0.0과 같음
r,g,b = 0.0 , 0.0 , 0.0

# Main 코드 부분

turtle.title('거북이로 그림 그리기')
turtle.shape('turtle')
#turtle.pensize(pSize)

# 좌클릭 1, 가운데 클릭 2, 우클릭 3
turtle.onscreenclick(screenLeftClick,1)
turtle.onscreenclick(screenMidClick,2)
turtle.onscreenclick(screenRightClick,3)

turtle.done()
