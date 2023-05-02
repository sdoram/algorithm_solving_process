# https://www.acmicpc.net/problem/1284

# 숫자 사이의 여백 1cm
# 1은 2cm, 0은 4cm , 나머지 숫자는 3cm
# 판의 경계와 숫자 사이는 1cm
while True:
    # 입력이 0일 때까지 지속
    num = input()
    if num == '0':
        break
    # 양쪽 여백 + 판의 경계
    answer = len(num)-1+2
    for n in num:
        if n == '1':
            answer += 2
        elif n == '0':
            answer += 4
        else:
            answer += 3
    print(answer)
