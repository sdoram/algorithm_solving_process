# https://www.acmicpc.net/problem/2576

num_list = []
for _ in range(7):
    num_list.append(int(input()))
num_list = sorted([num for num in num_list if num % 2 != 0])
if len(num_list) == 0:
    print(-1)
else:
    print(sum(num_list))
    print(num_list[0])
