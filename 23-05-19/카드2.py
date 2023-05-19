# https://www.acmicpc.net/problem/2164

# 1 1
# 2 2
# 3 2
# 4 4
# 5 2
# 6 4
# 7 6
# 8 8
# 9 2
# 10 4
# 11 6
# 12 8
# 13 10
# 14 12
# 15 14
# 16 16
# 17 2
# 18 4
# 19 6
# 20 8

N = 16
N = int(input())
# set으로 remove 시간 효율 상승
N_set = set(list(range(1, N + 1)))
COUNT = 0
while len(N_set) != 1:
    # set이 해시테이블로 순서를 구성하므로
    # sorted()로 혹시 바뀐 순서들 재정렬
    for num in sorted(list(N_set)):
        COUNT += 1
        if COUNT % 2 == 1:
            N_set.remove(num)
print(*N_set)
