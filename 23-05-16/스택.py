# https://www.acmicpc.net/problem/10828
# push append()
# size len()
# empty 0 if stack else 1
# pop pop() if pop() else -1
# top [-1] if [-1] else -1

from sys import stdin

stack_list = []
for _ in range(int(stdin.readline())):
    command = list(stdin.readline().split())
    if command[0] == "push":
        stack_list.append(int(command[1]))
    elif command[0] == "size":
        print(len(stack_list))
    elif command[0] == "empty":
        print(0 if stack_list else 1)
    try:
        if command[0] == "pop":
            print(stack_list.pop())
        elif command[0] == "top":
            print(stack_list[-1])
    except IndexError:
        print(-1)
