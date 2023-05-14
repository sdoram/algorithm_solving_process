# https://www.acmicpc.net/problem/3036
from fractions import Fraction

N = int(input())
rings = list(map(int, input().split()))
for num in range(1, len(rings)):
    number = Fraction(rings[0], rings[num])
    print(str(number.numerator), "/", str(number.denominator), sep="")
