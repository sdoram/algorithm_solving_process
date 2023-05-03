# https://www.acmicpc.net/problem/1076


color_dict = {
    'black': [0, 1],
    'brown': [1, 10],
    'red':	[2, 100],
    'orange': [3, 1000],
    'yellow': [4, 10000],
    'green': [5, 100000],
    'blue':	[6, 1000000],
    'violet': [7, 10000000],
    'grey':	[8, 100000000],
    'white': [9, 1000000000]
}
# 입력은 세가지 색
# 처음 두가지는 저항 값, 마지막 하나는 곱
# a = input()
# b = input()
# c = input()
a = 'yellow'
b = 'violet'
c = 'red'

a = 'orange'
b = 'red'
c = 'blue'

a = 'white'
b = 'white'
c = 'white'
# 처음 두개는 [0]번째를 받아서 저항값을 받고 마지막은 [1]번째로 곱받기
# a*10으로 10의 자리로 바꾸기
print((color_dict[a][0]*10 + color_dict[b][0])*color_dict[c][1])
