# https://www.acmicpc.net/problem/1350
from sys import stdin

N = 1
DATA = [16, 32, 128, 128, 0]
STORAGE = 32768

# 제출 코드
N = int(stdin.readline())
DATA = list(map(int, stdin.readline().split()))
STORAGE = int(stdin.readline())
# (n-1) // m+1 자주 애용하는 소수점 올림 효과
print(sum([((data - 1) // STORAGE + 1) * STORAGE for data in DATA]))
