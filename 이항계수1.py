# https://www.acmicpc.net/problem/11050

# 5개의 숫자중 2개를 뽑는 경우의 수 10개
# 5! // 2!(5-2)!
# 120 // 12
# 이항계수의 식을 보고 코드로 작성하는 건 쉬웠는데
# 수식 자체가 아직 이해안된다.

# 팩토리얼 구하기 함수
def factorial(num):
    number = 1
    for n in range(1, num+1):
        number *= n
    return number


N, K = map(int, input().split())
n = factorial(N)
r = factorial(K)
n_r = factorial(N-K)
print(n // (r*n_r))
