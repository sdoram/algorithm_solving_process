# https://www.acmicpc.net/problem/11656
S = input()
word_list = []
for word in range(len(S)):
    word_list.append(S[word:])
print(*sorted(word_list), sep="\n")
