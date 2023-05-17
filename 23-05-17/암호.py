# https://www.acmicpc.net/problem/1855

# 홀수는 정방향
# 짝수는 역방향

K = 3
WORD = "aeijfbcgklhd"
NEW_WORD = []
for n in range(len(WORD) // K):
    if n % 2 == 0:
        # 홀수는 정방향 입력받기
        NEW_WORD.append(WORD[n * K : (n + 1) * K])
    else:
        # 짝수는 역방향 입력받기
        REVERSE_WORD = WORD[n * K : (n + 1) * K]
        NEW_WORD.append(REVERSE_WORD[::-1])
WORD_LIST = []
# 각 원소를 분리하기 위해 2중 for문
for nw in NEW_WORD:
    word = []
    for w in nw:
        word.append(w)
    WORD_LIST.append(word)
# 분리된 원소를 가지고 zip으로 묶기
WORD_LIST = list(zip(*WORD_LIST))
FIRST_WORD = ""
# WORD_LIST의 원소가 튜플이라서 풀기 위해 for문
for word in WORD_LIST:
    FIRST_WORD += "".join(word)
print(FIRST_WORD)
# zip 써보겠다고 무슨 코드를 만든거냐

K = int(input())
WORD = input()
NEW_WORD = []
for n in range(len(WORD) // K):
    if n % 2 == 0:
        # 홀수는 정방향 입력받기
        NEW_WORD.append(WORD[n * K : (n + 1) * K])
    else:
        # 짝수는 역방향 입력받기
        REVERSE_WORD = WORD[n * K : (n + 1) * K]
        NEW_WORD.append(REVERSE_WORD[::-1])
ANSWER = ""
# 2중 for문으로 각 원소의 index순서에 맞게 뽑아오기
for NW in range(len(NEW_WORD[0])):
    for N in NEW_WORD:
        ANSWER += N[NW]
print(ANSWER)
