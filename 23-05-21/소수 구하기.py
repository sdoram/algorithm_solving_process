# https://www.acmicpc.net/problem/1929

# M, N = 3, 16

M, N = map(int, input().split())
# M=1인 경우 1이 출력되는 이슈 방지용 max() 사용
num_set = set([x for x in range(max(2, M), N + 1)])
for num in list(num_set):
    # 집합에 num이 존재하는지 체크
    if num in num_set:
        # num의 제곱근까지만 for문 진행
        for n in range(2, int(num**0.5) + 1):
            if num % n == 0:
                try:
                    # set의 remove이므로 시간복잡도 o(1)
                    num_set.remove(num)
                    break
                except KeyError:
                    break
    # 해시 테이블로 바뀐 순서 재정렬
print(*sorted(num_set), sep="\n")

# 에라토스테네스의 체
# M, N = 3, 16
M, N = map(int, input().split())
# 0과 1을 False로 설정
num_list = [False] * 2 + [True] * N
# int(N**0.5) +1으로 N의 제곱근까지 for문 설정
for num in range(2, int(N**0.5) + 1):
    # num_list[num]이 True라면
    if num_list[num]:
        # num의 배수 찾기
        for n in range(num + num, N + 1, num):
            # False로 소수 아님 처리
            num_list[n] = False
# 여러줄 출력을 위해 *, sep='\n' 사용
print(*[i for i in range(M, N + 1) if num_list[i]], sep="\n")
