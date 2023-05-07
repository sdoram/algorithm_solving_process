# https://www.acmicpc.net/problem/1357

def rev(x):
    rev_x = ''
    for num in x[::-1]:
        rev_x += num
    return int(rev_x)


X, Y = input().split()
print(rev(str(rev(X)+rev(Y))))
