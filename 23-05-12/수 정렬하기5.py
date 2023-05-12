# https://www.acmicpc.net/problem/15688
import sys

num_list = sorted([int(sys.stdin.readline()) for _ in range(int(input()))])
print(*num_list, sep="\n")
