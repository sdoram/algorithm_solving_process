# https://www.acmicpc.net/problem/11653
N = int(input())
n = 2
while N != 1:
    if N % n == 0:
        N //= n
        print(n)
        continue
    n += 1
