# https://www.acmicpc.net/problem/1145
# 5개의 자연수
import sys
num_list = [1, 2, 3, 4, 5]
num_list = [30, 42, 70, 35, 90]
num_list = [30, 45, 23, 26, 56]


def solution(num_list):
    num_list.sort()
    count = num_list[2]
    while True:
        answer = 0
        for num in num_list:
            # count가 num의 배수인 경우
            if count % num == 0:
                answer += 1
            # 그 경우가 3개가 된다면
            if answer == 3:
                return count
        count += 1


print(solution(list(map(int, sys.stdin.readline().split()))))
