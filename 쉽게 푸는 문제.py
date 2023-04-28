# 입력은 공백으로 구분되는 숫자 두 개
# 11을 한 번, 2를 두 번, 3을 세 번, 이런 식으로 1 2 2 3 3 3 4 4 4 4 5 수열을 만들고
# a ~ b번째 까지의 숫자를 더한 합을 출력
# sum, 반복문
find_start, find_end = map(int, input().split())
start, end = 1, 45
num_list = []

while start <= end:
    for num in range(start):
        num_list.append(start)
    start += 1
print(sum(num_list[find_start-1:find_end]))
# 수열 만드는 방법 바꿔보기
# print(len(num_list))
