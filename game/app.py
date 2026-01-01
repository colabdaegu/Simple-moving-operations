import tkinter as tk
import game.state as state
from game.logic import make_problem
from game.ui_canvas import draw_main, draw_winLose


class App():
    def __init__(self):  # 생성자

        state.w=tk.Canvas(state.window, width=400,height=600) # 너비 400, 높이 600, w에 캔버스 지정
        state.w.pack()

        state.w.create_rectangle(40,90,360,550,fill="whitesmoke") # 중앙 사각형
        state.object1=state.w.create_oval(state.x1, state.y1, state.x2, state.y2, fill="green") # 움직이는 대상(공)

        self.main()
        self.winLose_def()

        # 조작키
        b1=tk.Button(state.operation_window, text="▲",bg="goldenrod",command=self.up) # 위쪽으로 이동
        b2=tk.Button(state.operation_window, text="◀",bg="goldenrod",command=self.left) # 왼쪽으로 이동
        b3=tk.Button(state.operation_window, text="▼",bg="goldenrod",command=self.down) # 아래쪽으로 이동
        b4=tk.Button(state.operation_window, text="▶",bg="goldenrod",command=self.right) # 오른쪽으로 이동
        label1=tk.Label(state.operation_window, text="버튼으로",bg="snow")
        label2=tk.Label(state.operation_window, text="조작",bg="snow")

        b1.grid(row=0,column=1)  # 줄, 열
        b2.grid(row=1,column=0)
        b3.grid(row=1,column=1)
        b4.grid(row=1,column=2)
        label1.grid(row=0,column=3)
        label2.grid(row=1,column=3)

        self.computation()


    def main(self):
        draw_main(self)


    def saveNumber(self):  # 선택한 값들을 하나의 숫자로 정의
        # 선택한 값들을 하나의 숫자로 만들어 줌
        state.mainCount+=1
        if state.mainCount==1:
            state.result+=state.numbers  # 일의 자리 수
        elif state.mainCount>=2:
            state.result=state.result*10+state.numbers # 십의 자리 수 이상

        # inputValue 텍스트를 제거
        state.w.delete(state.inputValue)

        self.main()


    def computation(self):  # 문제 생성 및 계산
        math, state.compResult = make_problem()

        # 계산식 텍스트 표출
        state.compValue=state.w.create_text(200,185,text="문제: "+math+"=?",font=22)


    def winLose_def(self):  # 선택한 값이 맞거나 틀린 결과를 표출
        draw_winLose(self)


    def left(self):  # 왼쪽 입력 시
        state.w.delete(state.winLose)  # winLose 텍스트 제거

        # 움직이는 대상(공)이 벽에서 떨어져있거나 1,2,3,4,5칸에 도달했을 때
        if state.wall_x>40 or (state.wall_y>130-10 and state.wall_y<180-10 and state.wall_x>30) or (state.wall_y>200-10 and state.wall_y<250-10 and state.wall_x>30)or (state.wall_y>270-10 and state.wall_y<320-10 and state.wall_x>30) or (state.wall_y>340-10 and state.wall_y<390-10 and state.wall_x>30) or (state.wall_y>410-10 and state.wall_y<460-10 and state.wall_x>30):

            state.w.move(state.object1,-10,0)  # 움직이는 대상(공)을 x방향으로 -10만큼 이동
            state.wall_x-=10  # wall_x 값도 -10만큼 감소

            if (state.wall_y>130-10 and state.wall_y<180-10 and state.wall_x<40): # 1
                state.w.move(state.object1,160,0)  # 움직이는 대상(공)을 x방향으로 160만큼 이동
                state.wall_x=state.x1  # wall_x 값을 x1(190)으로 변경
                state.numbers=1
                self.saveNumber()

            elif (state.wall_y>200-10 and state.wall_y<250-10 and state.wall_x<40): # 2
                state.w.move(state.object1,160,0)  # 움직이는 대상(공)을 x방향으로 160만큼 이동
                state.wall_x=state.x1  # wall_x 값을 x1(190)으로 변경
                state.numbers=2
                self.saveNumber()

            elif (state.wall_y>270-10 and state.wall_y<320-10 and state.wall_x<40): # 3
                state.w.move(state.object1,160,0)  # 움직이는 대상(공)을 x방향으로 160만큼 이동
                state.wall_x=state.x1  # wall_x 값을 x1(190)으로 변경
                state.numbers=3
                self.saveNumber()


            elif (state.wall_y>340-10 and state.wall_y<390-10 and state.wall_x<40): # 4
                state.w.move(state.object1,160,0)  # 움직이는 대상(공)을 x방향으로 160만큼 이동
                state.wall_x=state.x1  # wall_x 값을 x1(190)으로 변경
                state.numbers=4
                self.saveNumber()

            elif (state.wall_y>410-10 and state.wall_y<460-10 and state.wall_x<40): # 5
                state.w.move(state.object1,160,0)  # 움직이는 대상(공)을 x방향으로 160만큼 이동
                state.wall_x=state.x1  # wall_x 값을 x1(190)으로 변경
                state.numbers=5
                self.saveNumber()
        else:
            # 경계면(x=40)에 도달하면 더이상 왼쪽으로 갈 수 없도록 wall_x값을 40으로 고정
            state.wall_x=40


    def right(self):  # 오른쪽 입력 시
        state.w.delete(state.winLose)  # winLose 텍스트 제거

        # wall_x는 공(object1)의 왼쪽 상단 좌표를 기준으로 하므로 공의 지름 20을 빼줌

        # 움직이는 대상(공)이 벽에서 떨어져있거나 6,7,8,9,0칸에 도달했을 때
        if state.wall_x<360-20 or (state.wall_y>130-10 and state.wall_y<180-10 and state.wall_x<370-20) or (state.wall_y>200-10 and state.wall_y<250-10 and state.wall_x<370-20) or (state.wall_y>270-10 and state.wall_y<320-10 and state.wall_x<370-20) or (state.wall_y>340-10 and state.wall_y<390-10 and state.wall_x<370-20) or (state.wall_y>410-10 and state.wall_y<460-10 and state.wall_x<370-20):

            state.w.move(state.object1,10,0)  # 움직이는 대상(공)을 x방향으로 10만큼 이동
            state.wall_x+=10  # wall_x 값도 10만큼 증가

            if (state.wall_y>130-10 and state.wall_y<180-10 and state.wall_x>360-20): # 6
                state.w.move(state.object1,-160,0)  # 움직이는 대상(공)을 x방향으로 -160만큼 이동
                state.wall_x=state.x1  # wall_x 값을 x1(190)으로 변경
                state.numbers=6
                self.saveNumber()

            elif (state.wall_y>200-10 and state.wall_y<250-10 and state.wall_x>360-20): # 7
                state.w.move(state.object1,-160,0)  # 움직이는 대상(공)을 x방향으로 -160만큼 이동
                state.wall_x=state.x1  # wall_x 값을 x1(190)으로 변경
                state.numbers=7
                self.saveNumber()

            elif (state.wall_y>270-10 and state.wall_y<320-10 and state.wall_x>360-20): # 8
                state.w.move(state.object1,-160,0)  # 움직이는 대상(공)을 x방향으로 -160만큼 이동
                state.wall_x=state.x1  # wall_x 값을 x1(190)으로 변경
                state.numbers=8
                self.saveNumber()

            elif (state.wall_y>340-10 and state.wall_y<390-10 and state.wall_x>360-20): # 9
                state.w.move(state.object1,-160,0)  # 움직이는 대상(공)을 x방향으로 -160만큼 이동
                state.wall_x=state.x1  # wall_x 값을 x1(190)으로 변경
                state.numbers=9
                self.saveNumber()

            elif (state.wall_y>410-10 and state.wall_y<460-10 and state.wall_x>360-20): # 0
                state.w.move(state.object1,-160,0)  # 움직이는 대상(공)을 x방향으로 -160만큼 이동
                state.wall_x=state.x1  # wall_x 값을 x1(190)으로 변경
                state.numbers=0
                self.saveNumber()
        else:
            # 경계면(x=360(-20))에 도달하면 더이상 오른쪽으로 갈 수 없도록 wall_x값을 340으로 고정
            state.wall_x=360-20


    def up(self):  # 위쪽 입력 시
        state.w.delete(state.winLose)  # winLose 텍스트 제거

        # 움직이는 대상(공)이 벽에서 떨어져있거나 '확인'칸에 도달했을 때
        if state.wall_y>90 or (state.wall_x>170-10 and state.wall_x<230-10 and state.wall_y>80):

            state.w.move(state.object1,0,-10)  # 움직이는 대상(공)을 y방향으로 -10만큼 이동
            state.wall_y-=10  # wall_y 값도 -10만큼 감소

            if (state.wall_x>170-10 and state.wall_x<230-10 and state.wall_y<90):  # '확인'칸에 도달했을 때
                state.w.move(state.object1,0,210)  # 움직이는 대상(공)을 y방향으로 210만큼 이동
                state.wall_y=state.y1  # wall_y 값을 y1(290)으로 변경

                if state.compResult==state.result:  # 문제 정답과 입력한 값이 동일할 때
                    state.rigList.append(state.result)  # rigList 리스트에 입력한 값을 추가
                    state.winLoseCount=1  # winLoseCount값을 1로 변경하여 화면에 '정답'텍스트 표시
                    state.w.delete(state.compValue)  # 캔버스에서 문제 텍스트를 제거

                    self.computation()

                    state.polygonColorCount+=1  # polygonColorCount값을 1만큼 더해서 create_polygon의 색깔을 변경
                    if state.polygonColorCount>4:
                        state.polygonColorCount=0  # 문제를 5번 넘게 맞추게 되면 create_polygon의 색깔을 다시 0부터 시작

                    self.winLose_def()


                else:
                    state.misList.append(state.result)  # misList 리스트에 입력한 값을 추가
                    state.winLoseCount=2  # winLoseCount값을 2로 변경하여 화면에 '틀렸음'텍스트 표시

                    self.winLose_def()


                # 기본값으로 수정
                state.result=0
                state.mainCount=0
                state.w.delete(state.inputValue)

                # 콘솔창에 정답과 오답 리스트 출력
                print("정답 : %s" %state.rigList)
                print("오답 : %s" %state.misList)
                print("="*20)

                self.main()

        else:
            # 경계면(y=90)에 도달하면 더이상 위쪽으로 갈 수 없도록 wall_y값을 90으로 고정
            state.wall_y=90


    def down(self):  # 아래쪽 입력 시
        state.w.delete(state.winLose)  # winLose 텍스트 제거

        # wall_y는 공(object1)의 왼쪽 상단 좌표를 기준으로 하므로 공의 지름 20을 빼줌

        # 움직이는 대상(공)이 벽에서 떨어져있거나 '지우기'칸에 도달했을 때
        if state.wall_y<550-20 or (state.wall_x>170-10 and state.wall_x<230-10 and state.wall_y<560-20):

            state.w.move(state.object1,0,10)  # 움직이는 대상(공)을 y방향으로 10만큼 이동
            state.wall_y+=10  # wall_y 값도 10만큼 증가
            if (state.wall_x>170-10 and state.wall_x<230-10 and state.wall_y>550-20):
                state.w.move(state.object1,0,-250)  # 움직이는 대상(공)을 y방향으로 -250만큼 이동
                state.wall_y=state.y1  # wall_y 값을 y1(290)으로 변경

                # 기본값으로 수정
                state.mainCount=0
                state.result=0
                state.w.delete(state.inputValue)


        else:
            # 경계면(y=550(-20))에 도달하면 더이상 아래쪽으로 갈 수 없도록 wall_y값을 530으로 고정
            state.wall_y=550-20


def run():
    app=App()
    state.operation_window.mainloop()
    state.window.mainloop()
