money = True

if money:
    print("택시 타고 귀귀씽")
else:
    print("걸어서 귀귀씽 ㅠㅠ")

if 1 in [1,2,3]:
    print("1 is in the list")
else:
    print("1 is not element of the list")

pocket = ['paper', 'trash', 'money']
if 'money' in pocket:
    pass # continue와 비슷한 용도
else:
    print("no money")


pocket = ['paper', 'card', 'trash']
if 'money' in pocket: print("taxi")
elif 'card': print("taxi")# else if 를 elif로 줄여서 사용한다!
else: print("걸어가") # 조건문 안에 문장이 한 줄이면 이처럼 조건문과 내부의 문장을 한줄로 표현 가능

score = 50
msg = 'success' if score>=60 else 'failure' # 이와같이 변수의 초기화도 한줄의 조건문으로 표현 가능
print(msg)