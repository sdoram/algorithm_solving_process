# https://www.acmicpc.net/problem/1264
vowels = ['a', 'e', 'i', 'o', 'u']
while True:
    count = 0
    word = input()
    if word == '#':
        break
    for w in word.lower():
        if w in vowels:
            count += 1
    print(count)
