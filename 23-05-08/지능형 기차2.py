# https://www.acmicpc.net/problem/2460

PERSONS = 0
person_list = []
for _ in range(10):
    quit_, riding = map(int, input().split())
    PERSONS += riding - quit_
    person_list.append(PERSONS)
print(max(person_list))
