# https://www.acmicpc.net/problem/7568

from sys import stdin

white_paper = [[False for _ in range(100)] for _ in range(100)]
for _ in range(int(stdin.readline())):
    black_paper = list(map(int, stdin.readline().split()))
    for i in range(black_paper[0], black_paper[0] + 10):
        for j in range(black_paper[1], black_paper[1] + 10):
            white_paper[i][j] = True
print(sum([sum(i) for i in white_paper]))
