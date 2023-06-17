# https://www.acmicpc.net/problem/10798
word_list = [[""] * 5 for _ in range(15)]
for i in range(5):
    words = list(input())
    for j, word in enumerate(words):
        word_list[j][i] = word
for words in word_list:
    print("".join(words), end="")
