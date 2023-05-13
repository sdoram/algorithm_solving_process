# https://www.acmicpc.net/problem/2720

# 25, 10, 5 , 1
for _ in range(int(input())):
    C = int(input())
    num_list = []
    Q, D, N, P = 25, 10, 5, 1
    num_list.append(C // Q)
    C = C % Q
    num_list.append(C // D)
    C = C % D
    num_list.append(C // N)
    C = C % N
    num_list.append(C // P)
    C = C % P
    print(*num_list)
