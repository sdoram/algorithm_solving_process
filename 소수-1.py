# https://www.acmicpc.net/problem/1312

# 입력 A분자 , B분모, N 소수점 자리
# (OverflowError)
from decimal import Decimal
# A, B, N = map(int, input().split())
# A, B, N = 1, 3, 100
A, B, N = 25, 7, 5
# A, B, N = 3, 4, 3
# A, B, N = 1, 4, 7
# A, B, N = 11, 14, 10000

# (OverflowError) 발생
A, B, N = map(int, input().split())
answer = str(int((A/B)*(10**N)))
print(answer[-1])

# 여전히 (OverflowError) 발생
A, B, N = map(int, input().split())
answer = str(Decimal(A/B*(10**N)))
print(answer.split('.')[1][0])

# 시간 초과
A, B, N = map(int, input().split())
answer = str(Decimal(A/B)*(10**N))
print(answer.split('.')[0][-1])
