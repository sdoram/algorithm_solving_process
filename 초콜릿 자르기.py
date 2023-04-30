# https://www.acmicpc.net/problem/2163

# N * M의 조각을 만드는 최소한의 숫자
# 입력은 N, M
# 출력은 최소한의 자르기
N, M = map(int, input().split())
print(N*M-1)

# 머릿속으로 생각해보고 암만 생각해도 이건데 싶은 생각에 해봤는데 정답이었다.
