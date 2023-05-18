# https://www.acmicpc.net/problem/4673
# 1~10000까지를 원소로 가진 리스트 만들기
num_list = [num for num in range(1, 10001)]
for num in range(1, 10001):
    # 10000을 넘는 경우 or 겹치는 경우를 위해 try, except
    try:
        # num과 num의 각 자리수의 합을 기준으로 remove
        num_list.remove(num + sum([int(n) for n in str(num)]))
    except ValueError:
        pass
    # 리스트 종방향으로 출력
print(*num_list, sep="\n")
