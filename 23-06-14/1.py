# https://www.acmicpc.net/problem/4375
from sys import stdin

while True:
    try:
        n = int(input())
        i = 1
        while i % n != 0:
            i *= 10
            i += 1
        print(len(str(i)))
    except EOFError:
        break

while True:
    try:
        n = int(stdin.readline().strip())
    except ValueError:
        break
    i = 1
    while i % n != 0:
        i = i * 10 + 1
    print(len(str(i)))
