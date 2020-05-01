# c, java에서는 변수의 자료형을 직접 지정해야하지만
# python에서는 변수에 저장된 값을 스스로 판단하여 자료형을 지정한다!

# 1. 변수 복사
print("(1) 주소값 까지 복사: var1 = var2")
a = [1,2,3]
print("list a       = {}".format(a))
print("address of a = {}".format(id(a))) # a의 주소값 출력 : id() 함수
b = a # list copy
print("list b       = {}".format(b))
print("address of b = {}".format(id(b))) # a list의 복사본인 b는 주소도 a와 같음을 알 수 있다.
# 즉, 같은 주소를 바라본다는 것은
# 복사본이든 원본이든 변경사항이 둘 다 적용됨!!
b.append(4)
print("list a = {}".format(a))
print("list b = {}".format(b))
print("a is b ? {}".format(a is b))

# b = a 방식으로 copy시, 값 뿐만 아니라 주소값 까지 복사됨!!

print("(2) 값만 복사1: var1 = var2[:]")
a = [1,2,3]
b = a[:]
# 주소값이 다름을 확인할 수 있다.
print("list a = {}".format(a))
print("list b = {}".format(b))
print("address of a = {}".format(id(a)))
print("address of b = {}".format(id(b))) 
print("a is b ? {}".format(a is b))

from copy import copy # import 해줘야됨
print("(3) 값만 복사2: var1 = copy(var2)")
a = [1,2,3]
b = copy(a)
# 주소값이 다름을 확인할 수 있다.
print("list a = {}".format(a))
print("list b = {}".format(b))
print("address of a = {}".format(id(a)))
print("address of b = {}".format(id(b))) 
print("a is b ? {}".format(a is b))

# 4. 변수를 선언하는 방법이 훨씬 자유롭고 다양함
print("(4) 변수 선언하는 다양한 방법")
a, b = ('python', 'java') # (a, b) = 'python', 'java'와 같음
c, d = ['hello', 'world']
e = f = 'don'
print(a, b)
print(c, d)
print(e, f)
a, b = b, a # swap도 간단하게 이루어짐
print(a, b)