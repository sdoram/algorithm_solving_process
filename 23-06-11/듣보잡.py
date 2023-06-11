# https://www.acmicpc.net/problem/1764

# 듣지 못한 수 N
# 보지 못한 수 M
# 듣지도 못하고 보지도 못하면 출력
from sys import stdin

N, M = map(int, stdin.readline().split())
persons_set = set()
unknown_set = set()
for _ in range(N + M):
    name = stdin.readline().strip()
    if name not in persons_set:
        persons_set.add(name)
    else:
        unknown_set.add(name)
print(len(unknown_set))
print("\n".join(sorted(unknown_set)))

N, M = map(int, stdin.readline().split())
persons = {}
for _ in range(N + M):
    name = stdin.readline().strip()
    if name not in persons:
        persons[name] = 1
    else:
        persons[name] += 1
unknown_list = [i[0] for i in sorted(persons.items()) if i[1] == 2]
print(len(unknown_list))
print("\n".join(unknown_list))
