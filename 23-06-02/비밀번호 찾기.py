# https://www.acmicpc.net/problem/17219
from sys import stdin

M, N = map(int, stdin.readline().split())
site_dict = {}
for _ in range(M):
    m = stdin.readline().split()
    site_dict[m[0]] = m[1]

for _ in range(N):
    print(site_dict[stdin.readline().split()[0]])
