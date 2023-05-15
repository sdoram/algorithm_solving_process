# https://www.acmicpc.net/problem/25305
import sys

N, K = map(int, sys.stdin.readline().split())
score_list = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
print(score_list[K - 1])
