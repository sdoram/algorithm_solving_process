# https://www.acmicpc.net/problem/14912
n, d = input().split()
count = 0
for i in range(1, int(n) + 1):
    for j in str(i):
        if d in j:
            count += 1
print(count)

n, d = input().split()
print(sum([True for i in range(1, int(n) + 1) for j in str(i) if d in j]))
