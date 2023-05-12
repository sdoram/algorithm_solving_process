# https://www.acmicpc.net/problem/14916
two_won = 0
money = int(input())
min_answer = -1
while money >= 0:
    if money % 5 == 0:
        min_answer = money // 5 + two_won
        break
    money -= 2
    two_won += 1
print(min_answer)
