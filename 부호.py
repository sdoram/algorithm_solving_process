# https://www.acmicpc.net/problem/1247

# 입력 3개의 테스트 존재 N = 테스트 케이스 개수
# N 이후 N줄 동안 정수의 합 구하기*3
import sys
for _ in range(3):
    sum_num = 0
    N = int(sys.stdin.readline())
    for _ in range(N):
        sum_num += int(sys.stdin.readline())
    if sum_num > 0:
        print('+')
    elif sum_num == 0:
        print('0')
    else:
        print('-')
