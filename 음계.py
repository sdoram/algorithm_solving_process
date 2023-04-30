# https://www.acmicpc.net/problem/2920

# 1~8까지 오름차순 = ascending
# 1~8까지 내림차순 = descending
# 1~8까지 랜덤 = mixed

import sys

scale_list = list(map(int, sys.stdin.readline().split()))
sorted_scale_list = sorted(scale_list)
reversed_scale_list = sorted(scale_list, reverse=True)

if scale_list == sorted_scale_list:
    print("ascending")
elif scale_list == reversed_scale_list:
    print("descending")
else:
    print("mixed")
