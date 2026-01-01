import tkinter as tk
from random import randint

# 움직이는 대상(공)의 초기 지정 좌표
global x1  # 왼쪽 상단 x값
global y1  # 왼쪽 상단 y값
global x2  # 오른쪽 히단 y값
global y2  # 오른쪽 하단 y값

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



class App():
    def __init__(self):  # 생성자
        
        global w
        global object1
        
        w=tk.Canvas(window, width=400,height=600) # 너비 400, 높이 600, w에 캔버스 지정
        w.pack()
        
        
        w.create_rectangle(40,90,360,550,fill="whitesmoke") # 중앙 사각형
        object1=w.create_oval(x1, y1, x2, y2, fill="green") # 움직이는 대상(공)

        self.main()
        self.winLose_def()

        # 조작키
        b1=tk.Button(operation_window, text="▲",bg="goldenrod",command=self.up) # 위쪽으로 이동
        b2=tk.Button(operation_window, text="◀",bg="goldenrod",command=self.left) # 왼쪽으로 이동
        b3=tk.Button(operation_window, text="▼",bg="goldenrod",command=self.down) # 아래쪽으로 이동
        b4=tk.Button(operation_window, text="▶",bg="goldenrod",command=self.right) # 오른쪽으로 이동
        label1=tk.Label(operation_window, text="버튼으로",bg="snow")
        label2=tk.Label(operation_window, text="조작",bg="snow")

        b1.grid(row=0,column=1)  # 줄, 열
        b2.grid(row=1,column=0)
        b3.grid(row=1,column=1)
        b4.grid(row=1,column=2)
        label1.grid(row=0,column=3)
        label2.grid(row=1,column=3)

        self.computation()
        
        
        

    def main(self):
        global polygonColorCount  # create_polygon들의 색깔 목록을 분류
        global result  # 선택한 결과값들을 저장
        
        global mainCount  # 값을 받을 때마다 1씩 카운트
        global inputValue  # 입력값을 캔버스에 출력해주는 텍스트


        # polygonColorCount가 받는 값에 따라 create_polygon들의 색깔 변경
        if polygonColorCount==0:
            self.color1="greenyellow"
            self.color2="lime"
        elif polygonColorCount==1:
            self.color1="salmon"
            self.color2="red"
        elif polygonColorCount==2:
            self.color1="lightskyblue"
            self.color2="steelblue"
        elif polygonColorCount==3:
            self.color1="yellow"
            self.color2="gold"
        elif polygonColorCount==4:
            self.color1="mediumorchid"
            self.color2="blueviolet"

        # 폴리곤(다각형) 생성
        w.create_polygon(0,0,400,0,360,90,40,90,fill=self.color1)
        w.create_polygon(400,0,360,90,360,550,400,600,fill=self.color1)
        w.create_polygon(0,600,40,550,360,550,400,600,fill=self.color2)
        w.create_polygon(0,0,40,90,40,550,0,600,fill=self.color2)

        # 대각선 생성
        w.create_line(0,0,40,90)
        w.create_line(400,0,360,90)
        w.create_line(0,600,40,550)
        w.create_line(400,600,360,550)

        # 보조 선 생성
        w.create_line(360,90,360,550)
        w.create_line(40,550,360,550)

        # 작은 사각형 생성
        w.create_rectangle(170,40,230,90,fill="white")  # 확인
        w.create_rectangle(360,130,385,180,fill="white")  # 1
        w.create_rectangle(360,200,385,250,fill="white")  # 2
        w.create_rectangle(360,270,385,320,fill="white")  # 3
        w.create_rectangle(360,340,385,390,fill="white")  # 4
        w.create_rectangle(360,410,385,460,fill="white")  # 5
        w.create_rectangle(170,550,230,570,fill="white")  # 지우기
        w.create_rectangle(15,130,40,180,fill="white")  # 6
        w.create_rectangle(15,200,40,250,fill="white")  # 7
        w.create_rectangle(15,270,40,320,fill="white")  # 8
        w.create_rectangle(15,340,40,390,fill="white")  # 9
        w.create_rectangle(15,410,40,460,fill="white")  # 10

        # 작은 사각형과 중앙 사각형의 경계 부분을 하얀 선으로 덮음
        w.create_line(170,90,230,90,fill="white")  # 확인
        w.create_line(360,130,360,180,fill="white")  # 1
        w.create_line(360,200,360,250,fill="white")  # 2
        w.create_line(360,270,360,320,fill="white")  # 3
        w.create_line(360,340,360,390,fill="white")  # 4
        w.create_line(360,410,360,460,fill="white")  # 5
        w.create_line(170,550,230,550,fill="white")  # 지우기
        w.create_line(40,130,40,180,fill="white")  # 6
        w.create_line(40,200,40,250,fill="white")  # 7
        w.create_line(40,270,40,320,fill="white")  # 8
        w.create_line(40,340,40,390,fill="white")  # 9
        w.create_line(40,410,40,460,fill="white")  # 10

        # 작은 사각형 위에 텍스트 생성
        w.create_text(30,155,text="1")
        w.create_text(30,225,text="2")
        w.create_text(30,295,text="3")
        w.create_text(30,365,text="4")
        w.create_text(30,435,text="5")
        w.create_text(370,155,text="6")
        w.create_text(370,225,text="7")
        w.create_text(370,295,text="8")
        w.create_text(370,365,text="9")
        w.create_text(370,435,text="0")
        w.create_text(200,65,text="확인",font="Helvetica 16 bold")
        w.create_text(200,560,text="지우기",fill="red")


        # 입력값 화면에 표시
        if mainCount==0:
            self.inputValueText=""  # 값을 하나도 받지 않은 초기 상태에서는 inputValueText값을 공백으로 저장
        elif mainCount>=1:
            self.inputValueText=str(result)  # 받은 값을 inputValueText에 대입

        inputValue=w.create_text(200,155,text=self.inputValueText)  # 입력값 텍스트 생성



    def saveNumber(self):  # 선택한 값들을 하나의 숫자로 정의
        global result  # 입력값(int)
        global mainCount  # 값을 받을 때마다 1씩 카운트
        global inputValue  # 입력값 텍스트 표출

        # 선택한 값들을 하나의 숫자로 만들어 줌
        mainCount+=1
        if mainCount==1:
            result+=numbers  # 일의 자리 수
        elif mainCount>=2:
            result=result*10+numbers # 십의 자리 수 이상

        # inputValue 텍스트를 제거
        w.delete(inputValue)
        
        self.main()

        
    def computation(self):  # 문제 생성 및 계산
        global compResult  # 문제 정답
        global compValue  # 문제를 화면에 보여주는 텍스트


        # 문제에 사용될 2개의 숫자를 랜덤으로 생성
        ranNum1=randint(0,60)
        for i in range(1,10+1):
            if ranNum1%i==0:
                ranNum2=i

        # 문제에 사용될 부등호 지정 및 문제 정답 계산
        compNum=randint(0,3)
        if compNum==0:
            aSign="+"
            compResult=ranNum1+ranNum2  # 덧셈 문제
        elif compNum==1:
            aSign="-"
            compResult=ranNum1-ranNum2  # 뺄셈 문제
        elif compNum==2:
            aSign="×"
            compResult=ranNum1*ranNum2  # 곱셈 문제
        else:
            aSign="÷"
            compResult=ranNum1/ranNum2  # 나눗셈 문제

        # 계산식 생성
        math=str(ranNum1)+aSign+str(ranNum2)

        # 계산식 텍스트 표출
        compValue=w.create_text(200,185,text="문제: "+math+"=?",font=22)
        

    def winLose_def(self):  # 선택한 값이 맞거나 틀린 결과를 표출
        global winLoseCount  # winLose텍스트의 세부 목록을 분류
        global winLose  # 선택한 값이 맞는지 틀렸는지 알려주는 텍스트

        # winLoseCount가 받는 값에 따라 winLose텍스트의 세부 목록들을 변경
        if winLoseCount==0:
            self.winLoseX=200
            self.winLoseY=450
            self.winLoseText=""
            self.winLoseFont="20"
            self.winLoseColor="black"
        elif winLoseCount==1:
            self.winLoseX=150
            self.winLoseY=450
            self.winLoseText="정답"
            self.winLoseFont="Helvetica 50 bold"
            self.winLoseColor="gold"
        elif winLoseCount==2:
            self.winLoseX=250
            self.winLoseY=450
            self.winLoseText="틀렸음"
            self.winLoseFont="Helvetica 42"
            self.winLoseColor="red"

        # 선택한 값이 맞는지 틀렸는지 캔버스에 표시
        winLose=w.create_text(self.winLoseX,self.winLoseY,text=self.winLoseText,font=self.winLoseFont,fill=self.winLoseColor)

        
    def left(self):  # 왼쪽 입력 시
        global wall_x  # 벽넘기 방지를 위한 보조 좌표
        global numbers  # 각 항목별로 값을 지정
        global winLose  # 선택한 값이 맞는지 틀렸는지 알려주는 텍스트
        w.delete(winLose)  # winLose 텍스트 제거

        # 움직이는 대상(공)이 벽에서 떨어져있거나 1,2,3,4,5칸에 도달했을 때
        if wall_x>40 or (wall_y>130-10 and wall_y<180-10 and wall_x>30) or (wall_y>200-10 and wall_y<250-10 and wall_x>30)or (wall_y>270-10 and wall_y<320-10 and wall_x>30) or (wall_y>340-10 and wall_y<390-10 and wall_x>30) or (wall_y>410-10 and wall_y<460-10 and wall_x>30):

            w.move(object1,-10,0)  # 움직이는 대상(공)을 x방향으로 -10만큼 이동
            wall_x-=10  # wall_x 값도 -10만큼 감소
            
            if (wall_y>130-10 and wall_y<180-10 and wall_x<40): # 1
                w.move(object1,160,0)  # 움직이는 대상(공)을 x방향으로 160만큼 이동
                wall_x=x1  # wall_x 값을 x1(190)으로 변경
                numbers=1
                self.saveNumber()
                
            elif (wall_y>200-10 and wall_y<250-10 and wall_x<40): # 2
                w.move(object1,160,0)  # 움직이는 대상(공)을 x방향으로 160만큼 이동
                wall_x=x1  # wall_x 값을 x1(190)으로 변경
                numbers=2
                self.saveNumber()
                
            elif (wall_y>270-10 and wall_y<320-10 and wall_x<40): # 3
                w.move(object1,160,0)  # 움직이는 대상(공)을 x방향으로 160만큼 이동
                wall_x=x1  # wall_x 값을 x1(190)으로 변경
                numbers=3
                self.saveNumber()
                

            elif (wall_y>340-10 and wall_y<390-10 and wall_x<40): # 4
                w.move(object1,160,0)  # 움직이는 대상(공)을 x방향으로 160만큼 이동
                wall_x=x1  # wall_x 값을 x1(190)으로 변경
                numbers=4
                self.saveNumber()

            elif (wall_y>410-10 and wall_y<460-10 and wall_x<40): # 5
                w.move(object1,160,0)  # 움직이는 대상(공)을 x방향으로 160만큼 이동
                wall_x=x1  # wall_x 값을 x1(190)으로 변경
                numbers=5
                self.saveNumber()
        else:
            # 경계면(x=40)에 도달하면 더이상 왼쪽으로 갈 수 없도록 wall_x값을 40으로 고정
            wall_x=40


    def right(self):  # 오른쪽 입력 시
        global wall_x  # 벽넘기 방지를 위한 보조 좌표
        global numbers  # 각 항목별로 값을 지정
        global winLose  # 선택한 값이 맞는지 틀렸는지 알려주는 텍스트
        w.delete(winLose)  # winLose 텍스트 제거

        # wall_x는 공(object1)의 왼쪽 상단 좌표를 기준으로 하므로 공의 지름 20을 빼줌
        
        # 움직이는 대상(공)이 벽에서 떨어져있거나 6,7,8,9,0칸에 도달했을 때
        if wall_x<360-20 or (wall_y>130-10 and wall_y<180-10 and wall_x<370-20) or (wall_y>200-10 and wall_y<250-10 and wall_x<370-20) or (wall_y>270-10 and wall_y<320-10 and wall_x<370-20) or (wall_y>340-10 and wall_y<390-10 and wall_x<370-20) or (wall_y>410-10 and wall_y<460-10 and wall_x<370-20):
        
            w.move(object1,10,0)  # 움직이는 대상(공)을 x방향으로 10만큼 이동
            wall_x+=10  # wall_x 값도 10만큼 증가
            
            if (wall_y>130-10 and wall_y<180-10 and wall_x>360-20): # 6
                w.move(object1,-160,0)  # 움직이는 대상(공)을 x방향으로 -160만큼 이동
                wall_x=x1  # wall_x 값을 x1(190)으로 변경
                numbers=6
                self.saveNumber()
                
            elif (wall_y>200-10 and wall_y<250-10 and wall_x>360-20): # 7
                w.move(object1,-160,0)  # 움직이는 대상(공)을 x방향으로 -160만큼 이동
                wall_x=x1  # wall_x 값을 x1(190)으로 변경
                numbers=7
                self.saveNumber()
                
            elif (wall_y>270-10 and wall_y<320-10 and wall_x>360-20): # 8
                w.move(object1,-160,0)  # 움직이는 대상(공)을 x방향으로 -160만큼 이동
                wall_x=x1  # wall_x 값을 x1(190)으로 변경
                numbers=8
                self.saveNumber()
                
            elif (wall_y>340-10 and wall_y<390-10 and wall_x>360-20): # 9
                w.move(object1,-160,0)  # 움직이는 대상(공)을 x방향으로 -160만큼 이동
                wall_x=x1  # wall_x 값을 x1(190)으로 변경
                numbers=9
                self.saveNumber()
                
            elif (wall_y>410-10 and wall_y<460-10 and wall_x>360-20): # 0
                w.move(object1,-160,0)  # 움직이는 대상(공)을 x방향으로 -160만큼 이동
                wall_x=x1  # wall_x 값을 x1(190)으로 변경
                numbers=0
                self.saveNumber()
        else:
            # 경계면(x=360(-20))에 도달하면 더이상 오른쪽으로 갈 수 없도록 wall_x값을 340으로 고정
            wall_x=360-20
            

    def up(self):  # 위쪽 입력 시
        global wall_y  # 벽넘기 방지를 위한 보조 좌표
        global result  # 입력값(int)
        global mainCount  # 값을 받을 때마다 1씩 카운트
        
        global polygonColorCount  # create_polygon들의 색깔 목록을 분류
        
        global compResult  # 문제 정답
        global compValue  # 문제를 화면에 보여주는 텍스트
        global inputValue  # 입력값 텍스트
        
        global winLoseCount  # winLose텍스트의 세부 목록을 분류
        global winLose  # 선택한 값이 맞는지 틀렸는지 알려주는 텍스트
        w.delete(winLose)  # winLose 텍스트 제거

        # 움직이는 대상(공)이 벽에서 떨어져있거나 '확인'칸에 도달했을 때
        if wall_y>90 or (wall_x>170-10 and wall_x<230-10 and wall_y>80):
            
            w.move(object1,0,-10)  # 움직이는 대상(공)을 y방향으로 -10만큼 이동
            wall_y-=10  # wall_y 값도 -10만큼 감소
            
            if (wall_x>170-10 and wall_x<230-10 and wall_y<90):  # '확인'칸에 도달했을 때
                w.move(object1,0,210)  # 움직이는 대상(공)을 y방향으로 210만큼 이동
                wall_y=y1  # wall_y 값을 y1(290)으로 변경
                
                if compResult==result:  # 문제 정답과 입력한 값이 동일할 때
                    rigList.append(result)  # rigList 리스트에 입력한 값을 추가
                    winLoseCount=1  # winLoseCount값을 1로 변경하여 화면에 '정답'텍스트 표시
                    w.delete(compValue)  # 캔버스에서 문제 텍스트를 제거
                    
                    self.computation()
                    
                    polygonColorCount+=1  # polygonColorCount값을 1만큼 더해서 create_polygon의 색깔을 변경
                    if polygonColorCount>4:
                        polygonColorCount=0  # 문제를 5번 넘게 맞추게 되면 create_polygon의 색깔을 다시 0부터 시작
                        
                    self.winLose_def()

                    
                else:
                    misList.append(result)  # misList 리스트에 입력한 값을 추가
                    winLoseCount=2  # winLoseCount값을 2로 변경하여 화면에 '틀렸음'텍스트 표시
                    
                    self.winLose_def()


                # 기본값으로 수정
                result=0
                mainCount=0
                w.delete(inputValue)

                # 콘솔창에 정답과 오답 리스트 출력
                print("정답 : %s" %rigList)
                print("오답 : %s" %misList)
                print("="*20)
                
                self.main()
                
        else:
            # 경계면(y=90)에 도달하면 더이상 위쪽으로 갈 수 없도록 wall_y값을 90으로 고정
            wall_y=90

            
    def down(self):  # 아래쪽 입력 시
        global wall_y  # 벽넘기 방지를 위한 보조 좌표
        global result  # 입력값(int)
        global mainCount  # 값을 받을 때마다 1씩 카운트
        
        global inputValue  # 입력값 텍스트
        
        global winLose  # 선택한 값이 맞는지 틀렸는지 알려주는 텍스트
        w.delete(winLose)  # winLose 텍스트 제거


        # wall_y는 공(object1)의 왼쪽 상단 좌표를 기준으로 하므로 공의 지름 20을 빼줌
        
        # 움직이는 대상(공)이 벽에서 떨어져있거나 '지우기'칸에 도달했을 때
        if wall_y<550-20 or (wall_x>170-10 and wall_x<230-10 and wall_y<560-20):
            
            w.move(object1,0,10)  # 움직이는 대상(공)을 y방향으로 10만큼 이동
            wall_y+=10  # wall_y 값도 10만큼 증가
            if (wall_x>170-10 and wall_x<230-10 and wall_y>550-20):
                w.move(object1,0,-250)  # 움직이는 대상(공)을 y방향으로 -250만큼 이동
                wall_y=y1  # wall_y 값을 y1(290)으로 변경

                # 기본값으로 수정
                mainCount=0
                result=0
                w.delete(inputValue)
                
                
        else:
            # 경계면(y=550(-20))에 도달하면 더이상 아래쪽으로 갈 수 없도록 wall_y값을 530으로 고정
            wall_y=550-20




app=App()
operation_window.mainloop()
window.mainloop()
