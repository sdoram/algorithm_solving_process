# https://www.acmicpc.net/problem/11399

# 이전 사람이 걸린 시간을 대기 시간으로 합해서 계산
# 인출 시간이 주어짐
# 오름차순 정렬 후
# 모두 더하는 게 가장 짧음
N = int(input())
num_list = sorted(list(map(int, input().split())))
print(sum([sum(num_list[: num + 1]) for num in range(N)]))
