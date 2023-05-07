# https://www.acmicpc.net/problem/2455
num = 0
max_num = 0
for _ in range(4):
    n, m = map(int, input().split())
    num += -n + m
    if max_num < num:
        max_num = num
print(max_num)
