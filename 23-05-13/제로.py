# https://www.acmicpc.net/problem/10773

import sys


num_list = []
for _ in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())
    num_list.pop() if not num else num_list.append(num)
print(sum(num_list))
