# https://www.acmicpc.net/problem/1259


def palindrome(num):
    for i1, n1 in enumerate(num):
        for i2, n2 in enumerate(num[::-1]):
            if i1 == i2:
                if n1 != n2:
                    return 'no'
    return 'yes'


# while문으로 반복해야 하는데 break 지점 설정에서 어려움을 겪음
# while문을 함수 실행으로 옮기고 함수 형태로 작성하면서 return 사용
while True:
    num = input()
    if num == '0':
        break
    print(palindrome(num))
