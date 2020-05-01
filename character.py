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