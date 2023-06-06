# https://www.acmicpc.net/problem/1769
X = input()
COUNT = 0
while len(X) > 1:
    X = str(sum(map(int, list(X))))
    COUNT += 1
print(COUNT, "YES" if int(X) % 3 == 0 else "NO", sep="\n")
