# 리스트 자료형
# list = [] 형식으로 선언하며, 배열의 요소로는 자료형에 관계없이 추가할 수 있다.
# list = [1, 2, "hello", "world"]
# list = []로 선언시 빈 list이며, list = list()로 선언하는 것과 같다.

# 1. list indexing
print("(1) list indexing")
list = [1,2,3]
print("list              = {}".format(list))
print("list[0]           = {}".format(list[0]))
print("list[0] + list[1] = {}".format(list[0]+list[1]))
print("list[-1]          = {}".format(list[-1]))

list = [1,2,3, ['a','b','c']]
print("list              = {}".format(list))
print("list[0]           = {}".format(list[0]))
print("list[0] + list[1] = {}".format(list[0]+list[1]))
print("list[-1]          = {}".format(list[-1])) # 배열안의 배열을 하나의 요소로 인식
print("list[-1][0]       = {}".format(list[-1][0])) # 배열안의 배열의 요소를 출력하기 위해서는 2차원 배열처럼 생각

list = [1,2,3, ['a','b','c', [4,5,6]]] # list안의 요소들의 자료형은 내부에서 알아서 판단해줌.
print("list              = {}".format(list))
print("list[0]           = {}".format(list[0]))
print("list[0] + list[1] = {}".format(list[0]+list[1]))
print("list[-1][0]       = {}".format(list[-1][0])) # 3중 배열에서 2번째 배열의 요소 출력
print("list[-1][-1][0]   = {}".format(list[-1][-1][0])) # 3중 배열에서 가장 안쪽의 배열 요소 출력

# 2. list slicing
print("(2) list slicing")
list = [1,2,3,4,5]
print("list[:2]    = {}".format(list[:2])) # list의 처음부터 2개의 요소 출력
print("list[2:]    = {}".format(list[2:])) # list의 index 2(3번쨰 요소)부터 끝까지 출력
list = [1,2, ['a','b','c']]
print("list[2][:1] = {}".format(list[2][:1])) # 중첩된 list에서도 slicing이 가능

# 3. list operation
a = [1,2,3]
b = [4,5,6]
print("(3) list operation")
print("list a   = {}".format(a))
print("list b   = {}".format(b))
print("list a+b = {}".format(a+b))
print("list b+a = {}".format(b+a)) # 문자열과 같이 + 연산시에 두 배열이 이어진다
print("list a*3 = {}".format(a*3)) # 문자열과 마찬가지로 * 연산시 곱해진 횟수만큼 출력된다.
print("len(a)   = {}".format(len(a))) # 문자열과 마찬가지로 len함수로 길이를 구한다.
# print("a[2]+'a' = {}".format(a[2]+'a')) # 오류!!!!
print("a[2]+'a' = {}".format(str(a[2])+'a')) # 3은 정수형으로 인식되고 a는 문자형으로 인식되기에, 3의 자료형을 바꿔야한다.


# 4. list 수정 및 삭제
print("(4) list 수정 및 삭제")
a = [1,2,3]
b = [1,2,3,4,5,6,7]
a[2] = 4
print("list a        = {}".format(a))
del a[2] # del 객체(간단하게 함수라고 생각)를 사용하여 요소 삭제
print("delete 4 in a     = {}".format(a))
a.append(4)
print("append 4 in a     = {}".format(a))
a.append([5,6])
print("append [5,6] in a = {}".format(a))
print("list b        = {}".format(b))
del b[3:]
print("del b[3:]     = {}".format(b)) # slicing 된 list도 제거할 수 있다.
c = [1,6,3,2,5,8,2]
print("original c = {}".format(c))
c.sort()
print("sorted c   = {}".format(c)) # 배열 정렬
c.reverse()
print("reversed c = {}".format(c)) # 배열 뒤집기
print("where is 6 = {}".format(c.index(6))) # 요소의 index 리턴, 요소가 아닌 경우 오류 발생
d = [1,2,3]
print("list d = {}".format(d))
d.insert(0, 0) # 0번 index에 요소 0 추가
d.insert(4, 0) # 4번 index에 요소 0 추가
print("list d = {}".format(d))

e = [1,2,3,1,2]
print("list e = {}".format(e))
e.remove(2) # 배열의 요소 중 전달받은 인자 제거(여러개 있는 경우 첫번째로 나온 인자 제거)
print("list e = {}".format(e))
print("pop e  = {}".format(e.pop())) # 배열의 마지막 요소 뽑고 배열에서 제거, 
                                     # 원하는 index를 매개변수로 전달해 해당 위치의 요소를 pop할 수도 있음
print("list e = {}".format(e))
print("count 1= {}".format(e.count(1))) # 문자열에서와 마찬가지로 list에 있는 지정한 요소의 개수를 리턴

a = [1,2,3]
b = [6,7]
print("list a = {}".format(a))
a.extend([4,5])
print("list a = {}".format(a))
a.extend(b)
print("list a = {}".format(a))

# extend와 append는 list에 요소를 추가한다는 공통점이 존재하지만
# append의 경우 여러 요소를 추가하지는 못한다(배열을 추가시에 배열 형태로 요소에 저장됨)
# extend의 경우 여러 요소를 한번에 추가할 수 있다(배열 형태로 추가해도 추가된 배열의 요소들이 추가됨)

# list 는 dataset에서도 많이 사용되므로 성질을 잘 이해할 것