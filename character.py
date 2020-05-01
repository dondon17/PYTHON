# 문자열
print("1. string representation")
str1 = "double quote is used when there are single(') quotes in string." # 큰 따옴표("") 사용해도 무관
str2 = 'single quote is used when there are double(") quotes in string' # 작은 따옴표('') 사용해도 무관
str3 = "\"my name is dowoon\"" # 이와 같이 백슬래시(\)를 이용해 같은 따옴표를 사용할 수 있다.
print(str1)
print(str2)
print(str3)

multiline = '''
line 1
line 2
line 3
''' 
# '''나 """의 역할은 하나의 문자열 변수에 여러 줄을 포함시킬 때 사용된다.
# 즉 /n, /t, /' 등의 백슬래시를 이용한 이스케이프 코드 없이 문자열에 탭 또는 개행을 추가할 수 있다.
print(multiline)

# 문자열 연산
print("2. string operation")
print("(1) concatenation - 더해서 연결")
# 1. concatenation (더해서 연결하기)
str1 = "Python"
str2 = " is fun!"
print("str1        : %s" %str1)
print("str2        : %s" %str2)
print("str1 + str2 : %s" %(str1+str2))

# 2. 문자열 곱하기
print("(2) multiplication - 곱한 횟수만큼 출력")
str1 = "a"
print("str1     : %s" %str1)
print("str1 * 5 : %s" %(str1*5))

# 3. 문자열 길이 구하기
print("(3) length of string - 문자열 길이")
str1 = "life is too short"
print("str1 = %s(length = %d)" %(str1, len(str1)))

# 4. 문자열 인덱싱 및 슬라이싱
print("(4) string indexing and slicing - 문자열에서의 index와 문자열 자르기")
str1 = "life is too short"
print("str1       = %s" %str1)
print("str1[0]    = %c" %str1[0]) # 다른 언어에서의 배열과 마찬가지로 index가 0부터 시작한다.
print("str1[-0]   = %c" %str1[-0])
print("str1[16]   = %c" %str1[16])
print("str1[-1]   = %c" %str1[-1]) # -는 뒤에서부터 인덱싱을 한다는 의미
print("str1[-2]   = %c" %str1[-2])
print("str1[0:4]  = %s" %str1[0:4]) # slicing - index 0부터 시작해 4개 문자 출력 즉 0<=index<4
print("str1[5:17] = %s" %str1[5:17]) # 5<=index<17
print("str1[0:]   = %s" %str1[0:]) # 끝지점 설정이 없을 시, 문자열의 끝까지 slicing
print("str1[0:]   = %s" %str1[:17]) # 시작지점 설정이 없을 시, 문자열의 처음부터 설정지점까지 출력
print("str1[0:-5]   = %s" %str1[0:-5]) # - indexing으로도 설정 가능

# 5. 문자열 일부 바꾸기
print("(5) change element(character) of string - immutable!!!")
str1 = "pithon"
print("str1    = %s" %str1)
print("str1[1] = %c" %str1[1])
# str1[1] = 'y' - 오류 발생!1 문자열의 요소값은 변경할 수 없다.(문자열이 immutable한 자료형이라고도 불리는 이유!)
str2 = str1[:1]+'y'+str1[2:] # 번거롭지만 이와같이 새로운 문자열을 생성하여 출력해야됨
print("str2 = %s" %str2)

# 6. 문자열 formatting
print("(6) string formatting")
print("I ate %d apples" %5)
print("I ate %s apples" %"five")
num = 5
five = "five"
print("I ate %d(%s) apples" %(num, five)) 
print("Error : %d%%" %0)
"""
이와같이 각 자료형에 맞게 formatting 코드를 입력해야한다
%s 문자열
%c 문자 1개
%d 정수(integer)
%f 실수(float)
%o 8진수
%x 16진수
%% %표현
"""
# 7. 문자열 정렬
print("(7) 문자열 정렬과 공백")
print("1. %10s" %"Hi") # 전체 길이가 10인 문자열 공간에서 대입되는 문자열을 오른쪽 정렬하고 남는 공간은 공백으로 채움
print("2. %-10s everyone" %"Hi") # -가 붙는 경우 길이가 10인 문자열 공간에서 왼쪽 정렬하고 남는 공간은 공백

# 8. 소수점 표현
print("(8) 소수 n번째 자리까지 표현")
print("%.4f" %3.141592432) # 소수 n번째까지 표현하기 위해서는 %.nf(%0.nf 도 가능)로 포매팅 코드 작성
print("%10.4f" %3.141592432) # 소수 n번째 까지 표현하되, 전체 길이가 10인 문자열 공간에서 오른쪽 정렬시킨다.
print("%-10.4f hi" %3.141592432) # 소수 n번째 까지 표현하되, 전체 길이가 10인 문자열 공간에서 왼쪽 정렬

# 9. format 함수를 사용해 formatting
print("(9) format function")
print("I ate {0} apples".format(3))
print("I ate {0} apples".format("five")) # 중괄호 안의 내용을 format함수의 인자로 채움
print("I ate {}({}) apples".format(3, "three"))
num = 3
three = "three"
print("I ate {number}({string}) apples".format(number=num, string=three))
print("{:<10}everone".format("hi")) # 전체 길이가 10인 문자열 공간에서 왼쪽 정렬로 채움
print("{:>10}everone".format("hi")) # 전체 길이가 10인 문자열 공간에서 오른쪽 정렬로 채움
print("{:^10}everone".format("hi")) # 전체 길이가 10인 문자열 공간에서 가운데 정렬로 채움
print("{0:=>10}everone".format("hi")) # 전체 길이가 10인 문자열 공간에서 오른쪽 정렬로 채움(남는공간을 =으로 채움)
print("{0:=<10}everone".format("hi")) # 전체 길이가 10인 문자열 공간에서 왼쪽 정렬로 채움(남는공간을 =으로 채움)
print("{0:=^10}everone".format("hi")) # 전체 길이가 10인 문자열 공간에서 가운데 정렬로 채움(남는공간을 =으로 채움)
print("{:.4f}".format(3.141592531))
print("{:10.4f}".format(3.141592531))
print("{{}}".format())
name = "dowoon"
print(f'my name is do {name}') # f 문자열 포매팅 방식. 잘 안쓸거 같다...

# 10. 문자열 관련 함수들
print("(10) string function")
str1 = "hello"
print("h의 개수(count)           : %d" %str1.count('h')) # 문자열에서 인자로 전달받은 요소의 개수를 리턴
print("l의 위치1(find)           : %d" %str1.find('l')) # index 2,3에 위치하지만 처음으로 나온 위치를 리턴, 없는 경우 -1 리턴
print("o의 위치2(index)          : %d" %str1.index('o')) # find와 같은 역할하지만, 해당 문자가 없는 경우 오류 발생
print("문자 삽입(join)           : {}".format(",,,".join(str1))) # 각 요소 사이에 원하는 문자(또는 문자열) 삽입
print("대문자로 변경(upper)      : {}".format(str1.upper()))
print("소문자로 변경(lower)      : {}".format("HELLO".lower()))
print("왼쪽의 공백 제거(lstrip)  : {}".format("     hello     world    ".lstrip()))
print("오른쪽의 공백 제거(rstrip): {}".format("     hello     world    ".rstrip()))
print("양쪽의 공백 제거(strip)   : {}".format("     hello     world    ".strip()))
str1 = "life is too short"
print("문자열 분리(split)        : {}".format(str1.split()))
print("문자열 바꾸기(replace)    : {}".format(str1.replace("life", "tonight")))
