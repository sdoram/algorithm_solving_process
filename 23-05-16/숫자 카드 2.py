# https://www.acmicpc.net/problem/10816
# 시간복잡도를 위해 N 이후 주어지는 카드들 dict로 만들기
from sys import stdin

N = int(stdin.readline())
N_list = list(map(int, stdin.readline().split()))
N_dict = {}
M = int(stdin.readline())
M_list = list(map(int, stdin.readline().split()))
for num in N_list:
    if num not in N_dict:
        N_dict[num] = 1
    else:
        N_dict[num] += 1
print(*[N_dict[num] if num in N_dict else 0 for num in M_list])
