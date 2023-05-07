# https://www.acmicpc.net/problem/1356

# num = '1236'

def number(num):
    for n in range(1, len(num)):
        first_num = num[:n]
        last_num = num[n:]
        # 곱하기를 위한 최초 값
        f_num = int(first_num[0])
        l_num = int(last_num[0])
        # [0]번 인덱스를 제외한 나머지 for문
        for i in range(1, len(first_num)):
            f_num *= int(first_num[i])
        for j in range(1, len(last_num)):
            l_num *= int(last_num[j])
        if f_num == l_num:
            return 'YES'
    return 'NO'


print(number(input()))
# print(num[:n], num[n:])
