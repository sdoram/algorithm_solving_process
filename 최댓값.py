# https://www.acmicpc.net/problem/2566

# 9*9 크기의 이차원 배열
# 81개의 자연수 또는 0
# 최댓값을 찾고 최댓값의 행과 열을 출력
import sys
num_list = []
for _ in range(9):
    num_list.append(list(map(int, sys.stdin.readline().split())))
# num_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0]]
# 최초 최댓값과 최초 위치 설정
max_num = num_list[0][0]
max_num_location = [1, 1]

for i1, num1 in enumerate(num_list, 1):
    for i2, num2 in enumerate(num1, 1):
        if max_num < num2:
            max_num = num2
            max_num_location = [i1, i2]
print(max_num)
print(*max_num_location)
