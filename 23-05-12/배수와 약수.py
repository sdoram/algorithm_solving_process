# https://www.acmicpc.net/problem/5086

import sys

while True:
    num_list = list(map(int, sys.stdin.readline().split()))
    if sum(num_list) == 0:
        break
    if num_list[1] % num_list[0] == 0:
        print("factor")
    elif num_list[0] % num_list[1] == 0:
        print("multiple")
    else:
        print("neither")
