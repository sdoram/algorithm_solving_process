# https://www.acmicpc.net/problem/11931

import sys

N = int(input())
num_set = sorted(set([int(sys.stdin.readline()) for _ in range(N)]), reverse=True)
for num in num_set:
    print(num)
