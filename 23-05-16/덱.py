# https://www.acmicpc.net/problem/10866
# push_front insert(0, 값)
# push_back append()
# size len()
# empty 0 if list else -1
# pop_front pop(0) if pop(0) else -1
# pop_back pop() if pop() else -1
# front [0] if [0] else -1
# back [-1] if [-1] else -1
# deck이 아니라 Double Ended Queue
from sys import stdin

deque = []
for _ in range(int(stdin.readline())):
    command = list(stdin.readline().split())
    if command[0] == "push_front":
        deque.insert(0, command[1])
    elif command[0] == "push_back":
        deque.append(command[1])
    elif command[0] == "size":
        print(len(deque))
    elif command[0] == "empty":
        print(0 if deque else 1)
    try:
        if command[0] == "pop_front":
            print(deque.pop(0))
        elif command[0] == "pop_back":
            print(deque.pop())
        elif command[0] == "front":
            print(deque[0])
        elif command[0] == "back":
            print(deque[-1])
    except IndexError:
        print(-1)
