# tuple이란 list와 비슷하지만
# list는 대괄호[]로 둘러싸며, 요소들을 추가, 삭제, 수정, 생성 등이 가능하지만
# tuple은 소괄호()로 둘러싸며, 요소들을 변경할 수 없다.
# tuple = () 빈 tuple
# tuple = (1, ) 원소가 1개인 경우 콤마(,) 추가 필수
# tuple = (1, 2) 원소가 2개 이상인 경우 콤마 필요 없음
# tuple = 1, 2, 3 이와 같이 선언 가능
# tuple = ('a', 'b', ('c', 'd')) list처럼 tuple 내부에 tuple 존재 가능
# 값이 변하길 원하지 않다면 tuple 사용!!!!!! (실제 프로그램에서는 값이 변경되는 경우가 많으므로 list가 선호됨)
# del tuple[0] 또는 tuple[0] = 5 이처럼 값을 삭제하거나 수정하려고 하면 오류 발생

# 1. tuple 다루기
print("(1) tuple")
t1 = (1, 2, 'a', 'b')
t2 = (3, 4)
print("tuple t1      = {}".format(t1))
print("t1[0]         = {}".format(t1[0]))
print("t1[3]         = {}".format(t1[3]))
print("t1[:2]        = {}".format(t1[:2]))
print("t1[0] + t1[1] = {}".format(t1[0]+t1[1]))
print("t1 + t2       = {}".format(t1+t2))
print("t2*3          = {}".format(t2*3))
print("len(t2)       = {}".format(len(t2)))

# 값의 변경이 없는 연산 등에서는 tuple도 가능하다.