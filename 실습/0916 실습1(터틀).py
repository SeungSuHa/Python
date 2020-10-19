#파이썬에서 미리 제공해주는 예약어 import
import turtle

#터틀 모양을 사용함
turtle.shape('turtle')

#예약어 for과 반복할 때 통상적으로 사용하는 변수 i or j
#in range함수:범위 무조건 0부터 시작하고 4에서 -1까지 (0,4) > (4)로 생략가능 (4번 반복한다)
#기호 ":"다음에 무언가 올 수 있다 (자동으로 들여쓰기가 되고 들여쓰기를 잘못하면 오류가 난다)

for i in range(0,4):
    #터틀을 현재 위치에서 100 만큼 앞으로 가게한다
    turtle.forward(200)
    #터틀을 오른쪽으로 90도 만큼 회전한다
    turtle.right(90)

#터틀을 종료함
turtle.done()
