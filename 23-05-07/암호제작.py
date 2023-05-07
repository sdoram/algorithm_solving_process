# https://www.acmicpc.net/problem/1837

# 잠깐 타임
P, K = map(int, input().split())
n = 2
n_list = []
while True:
    if P % n == 0:
        numbers = sorted([P//n, n])
        break
    n += 1
if numbers[0] >= K:
    print('GOOD')
else:
    print('BAD', numbers[0])
