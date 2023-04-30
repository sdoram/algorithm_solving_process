# https://www.acmicpc.net/problem/2935

# +, *만 주어짐 10의 제곱꼴만 나옴
# 입력 A 정수
# 입력 연산자 + or *
# 입력 B 정수
# 출력 결과값

A = int(input())
Operator = input()
B = int(input())

print(A*B if Operator == '*' else A+B)
