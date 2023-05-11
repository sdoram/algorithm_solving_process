# https://www.acmicpc.net/problem/11723
# add = if not in
# remove = if in
# check = if in print(1or0)
# toggle = if not in add , if in remove
# all = {1,2,3...20}으로 집합 만들기
# empty = {}로 만들기
import sys

S = 0
for _ in range(int(input())):
    word = sys.stdin.readline().split()
    if word[0] == "add":
        S |= 1 << int(word[1])
    elif word[0] == "remove":
        S &= ~(1 << int(word[1]))
    elif word[0] == "check":
        print(1 if S & (1 << int(word[1])) != 0 else 0)
    elif word[0] == "toggle":
        S ^= 1 << int(word[1])
    elif word[0] == "all":
        S = (1 << 21) - 1
    elif word[0] == "empty":
        S = 0
    print(S)
