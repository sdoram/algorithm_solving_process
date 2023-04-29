# https://www.acmicpc.net/problem/2581
# 입력은 정수 M과 N
# 출력은 M이상 N이하의 소수의 합, 최솟값 출력, 없으면 -1 출력
# for 문으로 range(M,N+1)로 범위 설정
# 2중 for문으로 2부터 N+1까지 % == 0 진행

import sys
M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
prime_number_list = []

# M부터 N+1까지 for문 진행하도록 range설정
for num in range(M, N+1):
    # range()의 시작값을 안주면 0부터 시작하고
    # 2로 주면 num이 2 이하일 때 소수에 2가 포함이 안되므로
    # range 1부터 시작하고 if문에서 1인 경우 제외
    for i in range(1, num):
        if i != 1 and num % i == 0:
            break
        # if문에 조건을 더 설정하는 대신 +1로 위의 조건문 피하기
        if i+1 == num:
            prime_number_list.append(i+1)
# 빈 리스트면 False 원소가 존재하면 True 이용
if prime_number_list:
    print(sum(prime_number_list))
    print(prime_number_list[0])
else:
    print(-1)
