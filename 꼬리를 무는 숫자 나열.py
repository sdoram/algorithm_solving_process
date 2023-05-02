# https://www.acmicpc.net/problem/1598

# 표는 4줄짜리

# 테스트 코드
# N, M = 4, 35
# N, M = 4, 12
N, M = 21, 39
# N, M = 39, 20
# N, M = 7, 32

N, M = map(int, input().split())
# M을 큰 수로 고정
if N > M:
    N, M = M, N
# M과 N이 4의 배수일 때 값 보정하기 위한 -1
width = (M-1)//4 - (N-1)//4
# N이 더 높은 위치에 있을 때 -가 되는 것을 수정하기 위한 abs
length = abs(width*4+N - M)
print(width, length)
print(width+length)
