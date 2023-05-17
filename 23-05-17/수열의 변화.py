# https://www.acmicpc.net/problem/1551
A, K = map(int, input().split())
A = list(map(int, input().split(",")))
for _ in range(K):
    # 임시 리스트 생성
    instance_A = []
    for a in range(1, len(A)):
        # 결과값 리스트에 추가
        instance_A.append(A[a] - A[a - 1])
    # A 갱신
    A = instance_A
print(*A, sep=",")
# instance_A를 안쓰고 싶은데 방법을 모르겠다.
