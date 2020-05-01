# 집합 자료형 - set
# 집합에 관련된 것을 쉽게 처리하기 위해 만들어진 자료형

# 1. set
print("(1) set 선언 및 초기화")
s0 = set() # 비어 있는 집합
print("set s0 = {}".format(s0)) 
s1 = set([1,2,3]) # 집합에 list 추가
print("set s1 = {}".format(s1)) 
s2 = set("hello") # 집합에 문자열 입력
print("set s2 = {}".format(s2))
# 집합은 중복을 허용하지 않는다 - 집합의 성질!!
# 집합에는 순서가 존재하지 않는다 - 집합의 성질!!
# 순서가 존재하지 않기 때문에 인덱싱으로 요소에 접근할 수 없다!!
l2 = list(s2)
print("set s2 to list = {}".format(l2)) 
t2 = tuple(s2)
print("set s2 to tuple= {}".format(t2))
# tuple이나 list로 변환시 순서가 생기며, 이 때 인덱싱으로 요소에 접근할 수 있게된다.

# 2. set operation 
print("(2) set operation")
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([3, 4, 5, 6, 7, 8])
print("s1 AND s2 = {}".format(s1&s2)) # s1.intersection(s2)와 동일한 결과!
print("s1 OR s2  = {}".format(s1|s2)) # s1.union(s2)와 동일한 결과
print("s1 - s2   = {}".format(s1-s2)) # s1.difference(s2)와 동일하지만 s2.difference(s1)과는 다르다 - 차집합의 성질

# 3. set function
print("(3) set function")
s1 = set([1,2,3])
print("original set s1 = {}".format(s1))
s1.add(4) # add 함수로 값을 한개 추가할 수 있다.
print("add 4 to s1     = {}".format(s1))
s1.update([5,6,7]) # update함수로 여러개의 값을 한번에 추가할 수 있다.
print("add values to s1= {}".format(s1))
s1.remove(7) # remove함수를 이용해 값을 제거할 수 있다.
print("remove 7 from s1= {}".format(s1))

# 흔히 아는 집합이 set이라고 생각하면 된다!
# 교집합, 합집합 등의 집합간의 연산이 적용되고
# add, update, remove등의 함수로 집합의 원소를 수정할 수 있다.