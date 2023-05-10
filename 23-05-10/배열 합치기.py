# https://www.acmicpc.net/problem/11728

import sys
A, B = map(int, input().split())
A_num_list = list(map(int, sys.stdin.readline().split()))
A_num_list.extend(map(int, sys.stdin.readline().split()))
print(*sorted(A_num_list))
