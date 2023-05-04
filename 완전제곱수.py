# https://www.acmicpc.net/problem/1977

# 입력 정수 M과 N
# 정수 M과 N사이의 완전 제곱수의 합과 최솟값 구하기
M = 75
N = 80
# M = int(input())
# N = int(input())
num_list = [num*num for num in range(1, 101)]
answer_list = []
for num in range(M, N+1):
    if num in num_list:
        answer_list.append(num)
if answer_list == []:
    print(-1)
else:
    print(sum(answer_list))
    print(answer_list[0])
