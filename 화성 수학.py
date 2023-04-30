# https://www.acmicpc.net/problem/5355

# 화성 연산자 @ = *3 , % = +5 , # = -7
# 입력 T= 테스트 케이스의 수
# 한줄씩 정수와 화성 연산자
# 출력 한줄씩 결과값 소수점 둘째 자리까지 출력
import sys
T = int(sys.stdin.readline())
# T = 1
for _ in range(T):
    num = list(sys.stdin.readline().split())
# num = ['3', '@', '%']
# num = ['10.4', '#', '%', '@']
# num = ['8', '#']
    answer = 0
    for n in num:
        try:
            # float은 isdigit() == False임
            answer += float(n)
        except ValueError:
            if n == '@':
                answer *= 3
            elif n == '%':
                answer += 5
            else:
                answer -= 7
    print("{:.2f}".format(answer))
