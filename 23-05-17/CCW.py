# https://www.acmicpc.net/problem/11758
from sys import stdin

# 기울기
# m=\frac{y_{2}-y_{1}}{x_{2}-x_{1}}
# y2 - y1/ x2 - x1
# m1 = (P2[1] - P1[1]) / (P2[0] - P1[0])
# m2 = (P3[1] - P2[1]) / (P3[0] - P2[0])
# print(m1, m2)


P1 = list(map(int, stdin.readline().split()))
P2 = list(map(int, stdin.readline().split()))
P3 = list(map(int, stdin.readline().split()))

# 외적
V1 = [P2[0] - P1[0], P2[1] - P1[1]]
V2 = [P3[0] - P2[0], P3[1] - P2[1]]
vector_product = (V1[0] * V2[1]) - (V1[1] * V2[0])


if vector_product > 1:
    print(1)
elif vector_product == 0:
    print(0)
elif vector_product < 0:
    print(-1)
