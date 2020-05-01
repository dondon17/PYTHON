# c, java와 비슷하게 while문을 사용할 수 있음

cnt = 0
while cnt<10:
    print("cnt = {}".format(cnt))
    cnt += 1

drawinf = """1. add
2. del
3. list
4. quit"""
num = 0
while True: # 무한 루프
    print(drawinf)
    num = int(input("input >> ")) # int형 변수를 input() 입력하는 함수!! scanf같은 함수
    if num == 4:
        print("you choose 4....bye")
        break # break문의 역할은 C와 같다. 반복문을 빠져나오는 역할!!

a = 0
while a<10:
    a += 1
    if a%2 == 0: continue # pass를 사용해도 결과가 똑같다!
    print(a)