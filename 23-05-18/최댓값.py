# https://www.acmicpc.net/problem/2562

# 최초 제출
max_num = 0
for index in range(1, 10):
    a = int(input())
    if max_num < a:
        # if문을 통해서 최댓값 갱신
        max_num = a
        # 최댓값이 등장한 위치 갱신
        num_count = index
print(max_num)
print(num_count)

# max, index사용 리팩토링
from sys import stdin

num_list = [int(stdin.readline()) for _ in range(9)]
# 가장 큰수 찾기
print(max(num_list))
# 가장 큰수의 밸류값으로 index 찾기 + index가 0번부터 시작하므로 +1
print(num_list.index(max(num_list)) + 1)

# 이차원 배열로 최댓값에 순서 포함한 리스트 만들기
from sys import stdin

# for문에서 range()를 통해 몇 번째 숫자를 포함한 이차원 배열로 만들기
num_list = sorted([[int(stdin.readline()), i] for i in range(1, 10)])
# 가장 큰 수의 밸류값
print(num_list[-1][0])
# 가장 큰 수의 순서
print(num_list[-1][1])
