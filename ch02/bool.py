# boolean 자료형은 true false 값만을 가지는 자료형

# 1. 변수 선언 및 초기화
print("(1) 변수 선언 및 초기화")
a = True
b = False
print("a = {}".format(type(a)))
print("b = {}".format(type(b)))
print("1==1 ? {}".format(1==1))
print("2==1 ? {}".format(2==1))
print("2>=1 ? {}".format(2>=1))

# 2. 자료형의 참과 거짓
'''
"string" : true
""       : false
[1,2,3]  : true
[]       : false
()       : false
{}       : false
1        : true
0        : false
None     : false
'''

# list 자료형의 true, false를 확인하기 위함
# 빈 list로 조건문을 할 시, else문이 실행되며
# 아래와 같이 요소가 있는 list로 조건문을 작성시, if문의 print가 실행된다!
if [1,2,3]:
    print("true")
else:
    print("false")