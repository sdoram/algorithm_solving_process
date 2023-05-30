# https://www.acmicpc.net/problem/1343


BOARD = "XXXXXX"
BOARD = "XX.XX"
BOARD = "XXXX....XXX.....XX"
BOARD = "X"
BOARD = "XX.XXXXXXXXXX..XXXXXXXX...XXXXXX"
BOARD = input()
A, B = "AAAA", "BB"
ANSWER = BOARD.replace("XXXX", A).replace("XX", B)
if "X" not in ANSWER:
    print(ANSWER)
else:
    print(-1)
