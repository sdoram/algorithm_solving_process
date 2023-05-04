# https://www.acmicpc.net/problem/5585
# 1000원을 냈을 때 500, 100, 50, 10,5 ,1원을 최소한으로 받는 수

# price = 380
# change = 1000 - price
# 무식하게 elif문으로 모든 조건을 확인
change = 1000 - int(input())
answer = 0
while change != 0:
    answer += 1
    if change - 500 >= 0:
        change -= 500
    elif change - 100 >= 0:
        change -= 100
    elif change - 50 >= 0:
        change -= 50
    elif change - 10 >= 0:
        change -= 10
    elif change - 5 >= 0:
        change -= 5
    elif change - 1 >= 0:
        change -= 1
print(answer)

# list로 만들어서 in으로 체크
# 다만 시간 복잡도 살짝 - 인듯
change_list = [500, 100, 50, 10, 5, 1]
change = 1000 - int(input())
answer = 0
while change != 0:
    for num in change_list:
        if change - num >= 0:
            change -= num
            answer += 1
            break
print(answer)
