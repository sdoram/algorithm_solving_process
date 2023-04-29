# https://www.acmicpc.net/problem/13458
# 입력
# N개의 시험장
# 각 시험장의 응시자 수 A1 A2 A3 ... An
# A의 값이 다 다름
# 총 감독관이 커버가능한 응시자 B, 부 감독관이 커버 가능한 수 C
# 총 감독관은 각 시험장에 1명 이상 존재해야할 때 최소한의 감독관 수 구하기

import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B, C = map(int, sys.stdin.readline().split())

# 총감독관의 커버수를 뺀 리스트 만들기
students_list = [a-B for a in A]
# 총감독관의 숫자 세기
answer = len(students_list)
for students in students_list:
    # 총 감독관의 범위보다 학생수가 많은 경우
    if students > 0:
        # C+1을 해주면서 나머지 부분을 챙겨주고
        # students-1을 하면서 나머지가 없는 경우에서 에러 방지
        answer += (students-1) // C+1
print(answer)
