# https://www.acmicpc.net/problem/2941
word = input()
croatia_word_list = ["dz=", "c=", "c-", "d-", "lj", "nj", "s=", "z="]
for croatia in croatia_word_list:
    if croatia in word:
        word = word.replace(croatia, "1")
print(len(word))
