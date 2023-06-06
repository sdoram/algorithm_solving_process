# https://www.acmicpc.net/problem/1402
from sys import stdin

for _ in range(int(stdin.readline())):
    A, B = map(int, stdin.readline().split())
    num_list = []
    while A != 1:
        for i in range(2, A + 1):
            if A % i == 0:
                A //= i
                num_list.append(i)
                break
    print("yes" if sum(num_list) == B else "no")
