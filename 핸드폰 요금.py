# https://www.acmicpc.net/problem/1267
# Y = 30마다 10원 29초까지 10
# M = 60마다 15원 59초까지 15

# 입력 통화의 갯수 N
# 통화 시간 N개
N = int(input())
call = list(map(int, input().split()))
M = 0
Y = 0
for c in call:
    Y += (c // 30+1) * 10
    M += (c // 60+1) * 15
if M < Y:
    print(f'M {M}')
elif Y == M:
    print(f'Y M {M}')
else:
    print(f'Y {Y}')
