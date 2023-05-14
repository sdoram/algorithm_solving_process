# https://www.acmicpc.net/problem/2845
L, P = map(int, input().split())
person_list = list(map(int, input().split()))
error_list = []
for person in person_list:
    error_list.append(person - (L * P))
print(*error_list)
