# https://www.acmicpc.net/problem/11004

import sys
N, K = map(int, sys.stdin.readline().split())
num_list = sorted(list(map(int, sys.stdin.readline().split())))
print(num_list[K-1])
