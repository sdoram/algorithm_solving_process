# https://www.acmicpc.net/problem/2587

# 자연수 5개
# 평균값과 중앙값
# sum()//5
# sorted[2]

num_list = [int(input()) for _ in range(5)]
print(sum(num_list) // len(num_list))
print(sorted(num_list)[2])
