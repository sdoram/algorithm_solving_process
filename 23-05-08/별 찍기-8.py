# https://www.acmicpc.net/problem/2445
N = int(input())
for n in range(1, N):
    print(('*'*n)+(' '*(2*(N-n)))+('*'*n))
print('*'*N*2)
for n in range(1, N)[::-1]:
    print(('*'*n)+(' '*(2*(N-n)))+('*'*n))
# 시간 52ms

for n in range(1, N)[::-1]:
    n = ' '*(2*n)
    # {N*2}를 n으로 채우고 남는 양쪽(^)에 *로 채우기
    print(f"{n:*^{N*2}}")
print('*'*N*2)
for n in range(1, N):
    n = ' '*(2*n)
    print(f"{n:*^{N*2}}")
# 시간 40ms
