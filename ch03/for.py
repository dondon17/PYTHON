# 다른 언어들 보다 for문의 작성이 간단하다

# 1. 전형적인 for문
print("(1) 전형적인 for문")
list_ = ['one', 'two', 'three']
for i in list_:
    print(i)

# 2. for문 응용
print("(2) for문 응용1")
list_ = [(1,2), (3,4), (5,6)]
for (a,b) in list_: # 이와같이 form을 맞춰주면 된다.
    print(a+b)

# 3. for문 응용
print("(3) for문 응용2")
score_ = [90, 30, 66, 44, 85]
cnt = 0
for sc in score_:
    cnt +=1
    if sc>=60: print("%d번 학생: pass!" %cnt)
    else: print("%d번 학생: fail..." %cnt)

# 4. for문 응용
print("(4) for문 응용3")
score_ = [90, 30, 66, 44, 85]
cnt = 0
for sc in score_:
    cnt +=1
    if sc>=60: print("%d번 학생: pass!" %cnt)
    else: continue

# 5. range 함수 - 숫자 list를 생성해주는 함수
print("(5) range 사용")
for i in range(1, 10): # for i=1; i<10; i++와 같으며, range안에 인자가 하나인 경우 해당 인자 미만까지 반복!
    print(i)

score_ = [90, 30, 66, 44, 85]
for num in range(len(score_)):
    if score_[num] > 60: print("%d번 학생: pass!" %(num+1))
    else: continue

# 6. for문을 활용한 구구단 출력
print("(6) 9x9")
for i in range(2, 10):
    for j in range(1, 10):
        print("%d x %d = %d"%(i, j, i*j), end=" ") # end인자는 출력하고 개행하지 않고 출력하기 위함!!
    print("")

# 7. list comprehension
print("(7) list comprehension")
a = [1,2,3,4]
res = []
for num in a:
    res.append(num*2)
print(a)
print(res)
res = [num*3 for num in a] # 이와같이 list안에 for문을 사용해 원소를 생성할 수 있다.
print(res)