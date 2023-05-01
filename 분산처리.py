# https://www.acmicpc.net/problem/1009
import sys

# 시간 초과
T = int(sys.stdin.readline())
for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    total_num = str(a**b)
    print(int(total_num[-1]))

# 10을 체크하지 못했음
T = int(sys.stdin.readline())
for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    a1, b1 = int(str(a)[-1]), int(str(b)[-1])
    total_num = str(a1 ** b1)
    print(int(total_num[-1]))

# b가 한자리만 가지고는 제대로 결과가 안나옴
# print(pow(2, 10)) # 1024
# print(pow(2, 0)) # 1
# print(pow(2, 1)) # 2
T = int(sys.stdin.readline())
for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    a1, b1 = int(str(a)[-1]), int(str(b)[-1])
    total_num = str(a1 ** b1)
    if int(total_num[-1]) == 0:
        print(10)
    else:
        print(int(total_num[-1]))

T = int(sys.stdin.readline())
for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    a1, b1 = int(str(a)[-1]), int(str(b)[-2:])
    total_num = str(a1 ** b1)
    if int(total_num[-1]) == 0:
        print(10)
    else:
        print(int(total_num[-1]))
