# https://www.acmicpc.net/problem/16435
import sys

N, L = map(int, sys.stdin.readline().split())
fruits = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
while fruits:
    if L >= fruits.pop():
        L += 1
print(L)
