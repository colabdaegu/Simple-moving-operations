from random import randint

def make_problem():
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

    return math, compResult
