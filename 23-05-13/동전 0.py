# https://www.acmicpc.net/problem/11047

N, K = map(int, input().split())
num = 0
coin_list = sorted([int(input()) for _ in range(N)], reverse=True)
for coin in coin_list:
    num += K // coin
    K %= coin
print(num)
