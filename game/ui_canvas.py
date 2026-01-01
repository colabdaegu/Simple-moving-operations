import game.state as state

def draw_main(self):
    # polygonColorCount가 받는 값에 따라 create_polygon들의 색깔 변경
    if state.polygonColorCount==0:
        self.color1="greenyellow"
        self.color2="lime"
    elif state.polygonColorCount==1:
        self.color1="salmon"
        self.color2="red"
    elif state.polygonColorCount==2:
        self.color1="lightskyblue"
        self.color2="steelblue"
    elif state.polygonColorCount==3:
        self.color1="yellow"
        self.color2="gold"
    elif state.polygonColorCount==4:
        self.color1="mediumorchid"
        self.color2="blueviolet"

    # 폴리곤(다각형) 생성
    state.w.create_polygon(0,0,400,0,360,90,40,90,fill=self.color1)
    state.w.create_polygon(400,0,360,90,360,550,400,600,fill=self.color1)
    state.w.create_polygon(0,600,40,550,360,550,400,600,fill=self.color2)
    state.w.create_polygon(0,0,40,90,40,550,0,600,fill=self.color2)

    # 대각선 생성
    state.w.create_line(0,0,40,90)
    state.w.create_line(400,0,360,90)
    state.w.create_line(0,600,40,550)
    state.w.create_line(400,600,360,550)

    # 보조 선 생성
    state.w.create_line(360,90,360,550)
    state.w.create_line(40,550,360,550)

    # 작은 사각형 생성
    state.w.create_rectangle(170,40,230,90,fill="white")  # 확인
    state.w.create_rectangle(360,130,385,180,fill="white")  # 1
    state.w.create_rectangle(360,200,385,250,fill="white")  # 2
    state.w.create_rectangle(360,270,385,320,fill="white")  # 3
    state.w.create_rectangle(360,340,385,390,fill="white")  # 4
    state.w.create_rectangle(360,410,385,460,fill="white")  # 5
    state.w.create_rectangle(170,550,230,570,fill="white")  # 지우기
    state.w.create_rectangle(15,130,40,180,fill="white")  # 6
    state.w.create_rectangle(15,200,40,250,fill="white")  # 7
    state.w.create_rectangle(15,270,40,320,fill="white")  # 8
    state.w.create_rectangle(15,340,40,390,fill="white")  # 9
    state.w.create_rectangle(15,410,40,460,fill="white")  # 10

    # 작은 사각형과 중앙 사각형의 경계 부분을 하얀 선으로 덮음
    state.w.create_line(170,90,230,90,fill="white")  # 확인
    state.w.create_line(360,130,360,180,fill="white")  # 1
    state.w.create_line(360,200,360,250,fill="white")  # 2
    state.w.create_line(360,270,360,320,fill="white")  # 3
    state.w.create_line(360,340,360,390,fill="white")  # 4
    state.w.create_line(360,410,360,460,fill="white")  # 5
    state.w.create_line(170,550,230,550,fill="white")  # 지우기
    state.w.create_line(40,130,40,180,fill="white")  # 6
    state.w.create_line(40,200,40,250,fill="white")  # 7
    state.w.create_line(40,270,40,320,fill="white")  # 8
    state.w.create_line(40,340,40,390,fill="white")  # 9
    state.w.create_line(40,410,40,460,fill="white")  # 10

    # 작은 사각형 위에 텍스트 생성
    state.w.create_text(30,155,text="1")
    state.w.create_text(30,225,text="2")
    state.w.create_text(30,295,text="3")
    state.w.create_text(30,365,text="4")
    state.w.create_text(30,435,text="5")
    state.w.create_text(370,155,text="6")
    state.w.create_text(370,225,text="7")
    state.w.create_text(370,295,text="8")
    state.w.create_text(370,365,text="9")
    state.w.create_text(370,435,text="0")
    state.w.create_text(200,65,text="확인",font="Helvetica 16 bold")
    state.w.create_text(200,560,text="지우기",fill="red")

    # 입력값 화면에 표시
    if state.mainCount==0:
        self.inputValueText=""  # 값을 하나도 받지 않은 초기 상태에서는 inputValueText값을 공백으로 저장
    elif state.mainCount>=1:
        self.inputValueText=str(state.result)  # 받은 값을 inputValueText에 대입

    state.inputValue=state.w.create_text(200,155,text=self.inputValueText)  # 입력값 텍스트 생성


def draw_winLose(self):
    # winLoseCount가 받는 값에 따라 winLose텍스트의 세부 목록들을 변경
    if state.winLoseCount==0:
        self.winLoseX=200
        self.winLoseY=450
        self.winLoseText=""
        self.winLoseFont="20"
        self.winLoseColor="black"
    elif state.winLoseCount==1:
        self.winLoseX=150
        self.winLoseY=450
        self.winLoseText="정답"
        self.winLoseFont="Helvetica 50 bold"
        self.winLoseColor="gold"
    elif state.winLoseCount==2:
        self.winLoseX=250
        self.winLoseY=450
        self.winLoseText="틀렸음"
        self.winLoseFont="Helvetica 42"
        self.winLoseColor="red"

    # 선택한 값이 맞는지 틀렸는지 캔버스에 표시
    state.winLose=state.w.create_text(self.winLoseX,self.winLoseY,text=self.winLoseText,font=self.winLoseFont,fill=self.winLoseColor)
