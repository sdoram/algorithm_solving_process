# https://www.acmicpc.net/problem/1920
# 위에서 set으로 받고
# 밑의 리스트를 for문 돌면서 in으로 확인
from sys import stdin

N = stdin.readline()
find_set = set(list(map(int, stdin.readline().split())))
M = stdin.readline()
my_list = list(map(int, stdin.readline().split()))
for num in my_list:
    print(1 if num in find_set else 0)
