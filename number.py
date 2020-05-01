# 숫자형
a = 123
b = -53
print(a)
print(b)

# 실수형
a = 1.2
b = -3.14
print(a, b)

# 8진수, 16진수
a = 0o177 # 1*8^2 + 7*8^1 + 7*8^0
b = 0xabc # 10*16^2 + 11*16^1 + 12*16^0
print(a, b)

# 사칙연산
a = 7
b = 4
print("a + b = %d" %(a+b)) # 덧셈 연산
print("a - b = %f" %(a-b)) # 뺄셈 연산
print("a * b = %d" %(a*b)) # 곱셈 연산
print("a / b = %f" %(a/b)) # 나눗셈 연산(둘다 정수여도 실수로 출력 가능)
print("a // b = %f" %(a//b)) # 몫 연산
print("a ** b = %d" %(a**b)) # 지수승 연산 - a의 b승 출력
print("a %% b = %d" %(a%b)) # 나머지 연산 (mod)