# https://www.acmicpc.net/problem/2501

divisor_list = []
num, find_num = map(int, input().split())
for n in range(1, num+1):
    if num % n == 0:
        divisor_list.append(n)
try:
    print(divisor_list[find_num-1])
except IndexError:
    print(0)
