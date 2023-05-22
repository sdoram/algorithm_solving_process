# https://www.acmicpc.net/problem/5635
# 학생수 n
# 이름 d m y로 생일 주어짐
# 출력1 나이가 가장 적은 사람
# 출력2 나이가 가장 많은 사람
# sorted() d,m,y 순서로 진행

birthday_list = [list(input().split()) for _ in range(int(input()))]
for n in range(1, 4):
    birthday_list = sorted(birthday_list, key=lambda x: int(x[n]))
print(birthday_list[-1][0])
print(birthday_list[0][0])
