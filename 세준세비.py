# https://www.acmicpc.net/problem/1524

# import sys
# T = int(input())
# for _ in range(T):
#     # 테스트 케이스를 줄바꿈으로 구분 입력
#     input()
#     N, M = map(int, input().split())
#     # lstrip(), rstrip()으로 좌우 공백 제거
#     N_power = sorted(
#         list(map(int, sys.stdin.readline().lstrip().rstrip().split())))
#     M_power = sorted(
#         list(map(int, sys.stdin.readline().lstrip().rstrip().split())))
#     # N과 M이 0이 아닐때까지
#     while N and M:
#         if N_power[0] == M_power[0]:
#             M_power.pop(0)
#             M -= 1
#             continue
#         if N_power[0] < M_power[0]:
#             N_power.pop(0)
#             N -= 1
#         else:
#             M_power.pop(0)
#             M -= 1
#     print(f'S :{N_power}, B :{M_power}')
#     print('S' if N != 0 else 'B')


T = int(input())

for _ in range(T):
    input()
    N, M = map(int, input().split())
    # pop으로 가장 작은 수를 꺼내기 쉽도록 sorted(reverse=True)
    N_power = sorted(list(map(int, input().split())), reverse=True)
    M_power = sorted(list(map(int, input().split())), reverse=True)
    while len(N_power) and len(M_power):
        if N_power[-1] == M_power[-1]:
            M_power.pop()
            continue
        N_power.pop() if N_power[-1] < M_power[-1] else M_power.pop()
    print('S' if len(N_power) else 'B')
