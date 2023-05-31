# https://www.acmicpc.net/problem/1049
# N개의 끊어진 줄
# 기타줄은 1개씩 or 6개 구입 가능
# M개의 브랜드

# 끊어진 줄 N개와 M개의 브랜드
N, M = map(int, input().split())
min_package = 1000
min_single = 1000
for _ in range(M):
    package, single = map(int, input().split())
    min_package = min(min_package, package)
    min_single = min(min_single, single)

I, J = divmod(N, 6)

print(min(N * min_single, (I + 1) * min_package, I * min_package + J * min_single))


# 최초 값을 지정할 필요 없지만 시간 복잡도에서 -
# min_package = []
# min_single = []
# for _ in range(M):
#     package, single = map(int, input().split())
#     min_package.append(package)
#     min_single.append(single)

# min_package = min(min_package)
# min_single = min(min_single)

# 개별 단가가 더 싼경우
# if min_package / 6 > min_single:
#     print(N * min_single)
# #  패키지가 개별 단가로 사는 것보다 싼 경우
# elif min_package < min_single * J:
#     print((I + 1) * min_package)
# # 패키지 + 개별 단가인 경우
# else:
#     print(I * min_package + J * min_single)
