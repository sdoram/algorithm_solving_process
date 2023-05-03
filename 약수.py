# https://www.acmicpc.net/problem/1037

# 1과 자기 자신을 제외한 약수가 주어질 때 원래 숫자 구하기

num = int(input())
# sorted로 약수 오름차순 정렬하기
divisor_list = sorted(list(map(int, input().split())))
# 가장 작은 약수 * 가장 큰 약수 = 자기 자신
print(divisor_list[0]*divisor_list[-1])
