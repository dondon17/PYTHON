# 매개변수가 있는 함수
def add(a,b):
    return a+b

# 매개변수가 없는 함수
def say():
    return 'hi'

# 리턴값이 없는 함수
def add2(a,b):
    print("%d + %d = %d" %(a,b,a+b))

# 매개변수, 리턴값이 없는 함수
def say2():
    print("hello~")

print(add(1,2))
print(say())
add2(1,5)
say2()

# 이와같이 매개변수를 미리 지정하지 않고 전달할때 지정할 수도 있음
res = add(a=5, b=1)
print(res)

# 여러개의 매개변수를 받는 경우
def add3(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

res = add3(1,2,3,4,5,6,7,8,9,10)
print(res)

# 여러 형태의 매개변수를 받는 경우
def add4(choice, *args):
    if choice == 'add':
        sum=0
        for i in args:
            sum+=i
        return sum
    elif choice == 'mul':
        sum=1
        for i in args:
            sum*=i
        return sum

res1= add4('mul', 1,2,3,4,5)
res2= add4('add', 1,2,3,4,5)
print(res1, res2)

# 키워드 파라미터 kwargs -> dictionary자료형으로 만들어줌!!!
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1, b=2, foo='bar')

# 리턴값은 '하나'로 출력
def add5(a,b):
    return a+b, a*b

res = add5(3,5)
print(res) # 하나의 tuple자료형으로 표현됨

r1, r2 = add5(6, 5)
print(r1, r2) # 이와같이 설정하면 r1, r2에 순서대로 return값이 저장됨

# 매개변수에 초기값 미리 설정하기
def myself(name, old, man=True):
    print("name : {}".format(name))
    print("age  : {}".format(old))
    if man: print("man")
    else: print("woman")

myself('don', '24', False)

# 함수 안에서 값 변경하기
# 1. return값으로 초기화
a = 1
def vara(a):
    a += 1
    return a
a = vara(a)
print(a)

# 2. global 명령어 사용
a = 1
def var_a():
    global a
    a += 1

var_a()
print(a)

# 3. lambda 함수
sum = lambda a,b: a+b
print(sum(3,5))

# lambda는 약간 매크로 비슷한거 같다.