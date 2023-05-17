# https://www.acmicpc.net/problem/11866
# while문으로 길이가 같을 때까지 돌기
# 새롭게 리스트를 만들고 리스트의 내용물이
# 걸리면 pass 아니면 COUNT +1

from sys import stdin

# N, K = 7, 3
N, K = list(map(int, stdin.readline().split()))
N_list = list(range(1, N + 1))
K_list = []
COUNT = 0
while len(K_list) != N:
    # 중간에 N_list가 바뀌면 안되므로 깊은 복사 사용
    for n in N_list[::]:
        COUNT += 1
        if COUNT == K:
            N_list.remove(n)
            K_list.append(n)
            COUNT = 0
print(f"<{(str(K_list))[1:-1]}>")
