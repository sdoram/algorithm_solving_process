# https://www.acmicpc.net/problem/14241
# 슬라임을 합치면 x+y의 크기가 된다.
# 슬라임을 합치면 x*y의 점수를 얻는다.
# 출력은 최대 점수를 출력한다.
N = int(input()) - 1
slime_list = list(map(int, input().split()))
SCORE = 0
for _ in range(N):
    SCORE += slime_list[0] * slime_list[1]
    slime_list[0] += slime_list.pop(1)
print(SCORE)
