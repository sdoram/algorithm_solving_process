# https://www.acmicpc.net/problem/1252
bin_num = "1001101", "10010"
bin_num = input().split()
sum_num = int(bin_num[0], 2) + int(bin_num[1], 2)
# [2:]로 접두어 제거
print(bin(sum_num)[2:])
