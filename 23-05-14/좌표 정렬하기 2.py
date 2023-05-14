# https://www.acmicpc.net/problem/11651
import sys

N = int(sys.stdin.readline())
dot_list = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(N)])
dot_list = sorted(dot_list, key=lambda x: x[1])
for dot in dot_list:
    print(*dot)
