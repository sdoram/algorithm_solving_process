# https://www.acmicpc.net/problem/1057
N, A, B = 16, 8, 9
N, A, B = 60000, 101, 891
N, A, B = map(int, input().split())
COUNT = 1
while True:
    if A % 2 != 0 and A + 1 == B:
        print(COUNT)
        break
    else:
        A -= A // 2
        B -= B // 2
        COUNT += 1
