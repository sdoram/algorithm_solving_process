# https://www.acmicpc.net/problem/10866
# push_front insert(0, 값)
# push_back append()
# size len()
# empty 0 if list else -1
# pop_front pop(0) if pop(0) else -1
# pop_back pop() if pop() else -1
# front [0] if [0] else -1
# back [-1] if [-1] else -1

from sys import stdin

deck = []
for _ in range(int(stdin.readline())):
    command = list(stdin.readline().split())
    if command[0] == "push_front":
        deck.insert(0, command[1])
    elif command[0] == "push_back":
        deck.append(command[1])
    elif command[0] == "size":
        print(len(deck))
    elif command[0] == "empty":
        print(0 if deck else 1)
    try:
        if command[0] == "pop_front":
            print(deck.pop(0))
        elif command[0] == "pop_back":
            print(deck.pop())
        elif command[0] == "front":
            print(deck[0])
        elif command[0] == "back":
            print(deck[-1])
    except IndexError:
        print(-1)
