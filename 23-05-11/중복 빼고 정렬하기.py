# https://www.acmicpc.net/problem/10867

import sys

N = int(input())
N_list = sorted(set(map(int, sys.stdin.readline().split())))
print(*N_list)
