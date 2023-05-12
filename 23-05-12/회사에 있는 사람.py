# https://www.acmicpc.net/problem/7785
# 출입기록 n
# enter = 출근
# leave = 퇴근
import sys

commute_list = set()
for _ in range(int(input())):
    commute = sys.stdin.readline().split()
    if commute[1] == "enter":
        commute_list.add(commute[0])
    elif commute[1] == "leave":
        commute_list.remove(commute[0])
print(*sorted(commute_list, reverse=True), sep="\n")


# print(dir(set()))
