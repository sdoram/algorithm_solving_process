# https://www.acmicpc.net/problem/10826
f1 = 0
f2 = 1
n = int(input())
for _ in range(n):
    f1, f2 = f2, f1 + f2
print(f1)
