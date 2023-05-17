# https://www.acmicpc.net/problem/2164
# 제일 위를 버리고 2번째를 맨 밑으로 넣기 반복
# 마지막에 남는 카드 출력
# 첫 사이클 홀수 다 제거
# 계속해서 홀수자리 제거
# 이전 사이클의 마지막이 홀수인지 짝수인지 알아야함

# 시간 초과
N = int(input())
N_list = list(range(1, N + 1))
COUNT = 0
while len(N_list) != 1:
    COUNT += 1
    if COUNT % 2 == 1:
        for num in N_list[::]:
            N_list.remove(num)
    else:
        for num in N_list[::]:
            N_list.remove(num)
print(N_list[0])
