# https://www.acmicpc.net/problem/1676
N = int(input())
num = 1
for n in range(1, N + 1):
    num *= n
reverse_num = str(num)[::-1]
count = 0
for num in reverse_num:
    if num == "0":
        count += 1
    else:
        break
print(count)
