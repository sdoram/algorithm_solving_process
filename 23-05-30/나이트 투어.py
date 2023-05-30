# # https://www.acmicpc.net/problem/1331
import string

CHESS = set([str(i) + str(j) for i in string.ascii_uppercase[:6] for j in range(1, 7)])
for _ in range(36):
    try:
        CHESS.remove(input())
    except KeyError:
        break

print("Valid" if len(CHESS) == 0 else "Invalid")

# 오늘 배운 string을 import해서 사용한 것은 좋지만
# 이 문제가 요구하는 게 중복값을 체크하는 것으로 끝이 아닌 것 같다.
