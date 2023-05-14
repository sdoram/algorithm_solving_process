# https://www.acmicpc.net/problem/1026
# S = A[0] × B[0] + ... + A[N-1] × B[N-1]
# B에 가장 작은 수에 맞춰서 A는 가장 큰 수 대입
# A는 재배열, B는 재배열 불가
# 첫째 줄 N
# 둘째 줄 A
# 셋째 줄 B
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
new_b = []
answer = 0
for i, num in enumerate(B):
    new_b.append([num, i])
A.sort(reverse=True)
new_b.sort()
for n in range(N):
    answer += A[n] * new_b[n][0]
print(answer)
