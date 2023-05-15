# https://www.acmicpc.net/problem/2167
# 배열의 크기 N, M 2 3
# 배열 1 2 4
# 배열 8 16 32
# test case 3
# 1 1 2 3 1-1부터 2-3까지 더하기
# 1 2 1 2
# 1 3 2 3
import sys

N, M = 2, 3
# two_dimensional_array = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
two_dimensional_array = [[1, 2, 4], [8, 16, 32]]
print(*two_dimensional_array)
print([num for num in two_dimensional_array])
# for _ in range(sys.stdin.readline()):
for _ in range(3):
    answer = 0
    # i, j, x, y = sys.stdin.readline().split()
    i, j, x, y = 1, 1, 2, 3
    # answer = sum(two_dimensional_array[])
    print(two_dimensional_array[[i - 1][j - 1]])
# 1,1좌표와 2,3좌표를 가진 직사각형의 합을 구해야 함
