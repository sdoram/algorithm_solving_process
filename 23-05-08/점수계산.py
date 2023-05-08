# https://www.acmicpc.net/problem/2506
# 연속으로 맞으면 +1씩 추가 가산점
# answer = [1, 0, 1, 1, 1, 0, 0, 1, 1, 0]
T = int(input())
answer = list(map(int, input().split()))
SCORE = 0
TOTAL_SCORE = 0
for a in answer:
    if a:
        SCORE += 1
    else:
        SCORE = 0
    TOTAL_SCORE += SCORE
print(TOTAL_SCORE)
