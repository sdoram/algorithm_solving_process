# https://www.acmicpc.net/problem/1934

# 어디서 문제가 발생하는지 도저히 모르겠음
def get_gcd(A, B):
    # 무조건 A가 큰값 고정
    if A < B:
        A, B = B, A
    if A % B == 0:
        return B
    if A % B != 0:
        gcd = A % B
        while B % gcd != 0:
            B, gcd = gcd, B % gcd
    return gcd

    # A, B = 216, 126
    # A, B = 36, 64
for _ in range(int(input())):
    A, B = map(int, input().split())
    print(A*B//get_gcd(A, B))
