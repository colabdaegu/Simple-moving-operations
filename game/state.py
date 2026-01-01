import tkinter as tk

# 움직이는 대상(공)의 초기 지정 좌표
x1=190
y1=290
x2=210
y2=310

# 움직이는 대상(공)이 벽을 넘어가는 것을 막아주기 위해 wall_x와 wall_y 좌표 변수를 추가로 지정
wall_x=x1
wall_y=y1

result=0  # 선택한 값들을 저장

mainCount=0  # 값을 받을 때마다 1씩 카운트

winLoseCount=0  # 정답을 맞췄을 때와 틀렸을 때에 따라 바뀌는 값들을 분류 및 보조해주는 역할

polygonColorCount=0  # create_polygon들의 색깔 목록을 분류해주는 역할

# 정답값과 오답값을 저장하기 위한 리스트
rigList=[]
misList=[]

operation_window=tk.Tk()  # 조작을 위한 보조 윈도우
window=tk.Tk()  # 메인 윈도우

# 윈도우 타이틀
operation_window.title("조작키")
window.title("계산기 조작 게임")

w=None
object1=None

inputValue=None
compResult=None
compValue=None
winLose=None
numbers=0
