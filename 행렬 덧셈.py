# https: // www.acmicpc.net/problem/2738

# N, M 은 정수
# 주어지는 것은 N*M의 행렬 두 개
# N*M 크기의 행렬 두개의 원소를 각각 더한 행렬로 출력

# 이게 브론즈5가 맞나? 2차원 배열을 풀기 시작하니까 풀 수는 있는데
# 이제까지 배웠던 것들을 다 활용하니까 별로 안어려웠던거지 풀었던 브론즈5 중에 제일 어려운 것 같은데
import sys
N, M = 3, 3
N_M1 = [[1, 1, 1], [2, 2, 2], [0, 1, 0]]
N_M2 = [[3, 3, 3], [4, 4, 4], [5, 5, 100]]
answer = []
for I, N in enumerate(N_M1):
    num_list = []
    for i, n in enumerate(N):
        num = n + N_M2[I][i]
        num_list.append(num)
    answer.append(num_list)
for num in answer:
    print(*num)

N, M = map(int, sys.stdin.readline().split())
N_M1 = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
N_M2 = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

answer = []
for I, N in enumerate(N_M1):
    num_list = []
    for i, n in enumerate(N):
        num = n + N_M2[I][i]
        num_list.append(num)
    answer.append(num_list)
for num in answer:
    print(*num)
