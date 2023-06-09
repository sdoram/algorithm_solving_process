# https://www.acmicpc.net/problem/1380
# 사람 수 n
# n줄에 걸쳐 이름
# 2n -1 줄에 걸쳐 번호 + A or B
# 번호 등장 1번은 압수 2번은 돌려줌
# A or B가 필요한가?
# 0번이 나오면 테스트 종료
# case의 번호 필요
from sys import stdin

CASE = 0
while True:
    CASE += 1
    N = int(stdin.readline())
    if N == 0:
        break
    students = [stdin.readline().strip() for _ in range(N)]
    print(students)
    check_list = []
    for _ in range(N * 2 - 1):
        # 숫자와 함께 A or B가 같이 주어지나 숫자만 있으면 해결 가능
        check = int(stdin.readline().split()[0])
        # list comprehension에서 remove처럼 들어간 원소를 제거할 수 있는지?
        if check in check_list:
            check_list.remove(check)
        else:
            check_list.append(check)
        print(check_list)
    print(CASE, students[check_list[0] - 1])
