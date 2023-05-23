# https://www.acmicpc.net/problem/1158
from collections import deque

N, K = map(int, input().split())
deque_list = deque([n for n in range(1, N + 1)])
answer = []
for _ in range(N):
    # 시작값 조정 & -K +1로 popleft()으로 사라지는 숫자 고려
    deque_list.rotate(-K + 1)
    # popleft() == pop(0)이지만,
    # 연산 O(1) != O(N)
    answer.append(deque_list.popleft())
print(f'<{", ".join(map(str, answer))}>')

test_list = deque([i for i in range(1, 11)])
# 원형일 때 양수면 시계방향
test_list.rotate(1)
print(test_list)  # deque([10, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# 원형일 때 음수면 반 시계방향
test_list.rotate(-2)
print(test_list)  # deque([2, 3, 4, 5, 6, 7, 8, 9, 10, 1])
