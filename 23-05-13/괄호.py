# https://www.acmicpc.net/problem/9012

# ps = "(())())"


def parenthesis_string(ps):
    ps_dict = {"(": 0, ")": 0}
    for p in ps:
        ps_dict[p] += 1
        if ps_dict["("] < ps_dict[")"]:
            return "NO"
    return "YES" if ps_dict["("] == ps_dict[")"] else "NO"


for _ in range(int(input())):
    print(parenthesis_string(input()))
# print(ps_dict)
# 마지막에 개수가 다른 경우
# for 문 도중 )가 더 많아지는 경우
