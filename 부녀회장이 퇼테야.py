# https://www.acmicpc.net/problem/2775

# k = 층수, n = 호수
# 0층 존재 0층은 i호에 i명만큼 살고있음
# [1], [+1], [3,4,5]
# 1 2 3 4 5
# 1 3 6 10 15
# 1 4 10 20 35
# 1 5 15 35 70
# 1 6 21 56 126
k, n = 1, 3
k, n = 4, 5
for _ in range(int(input())):
    num_list1 = []
    num_list2 = []
    persons = 0
    k = int(input())
    n = int(input())
    # 0층 사람 만들기
    for num in range(1, n+1):
        persons += num
        num_list1.append(persons)
    # k층 구하기
    for _ in range(k-1):
        for idx, num in enumerate(num_list1, 1):
            # k-1층에서 1~n호까지의 사람 더하기
            num_list2.append(sum(num_list1[:idx]))
        num_list1 = num_list2
        num_list2 = []
    print(num_list1[-1])
