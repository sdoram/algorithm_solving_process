# https://www.acmicpc.net/problem/1251

# 글자를 임의의 부분을 2개 나눠서 3개의 단어로 만들기
# 3개의 단어의 앞뒤를 뒤집기
# 만들 수 있는 단어 중 가장 사전순으로 앞선 단어 만들기

# 첫 글자가 a와 가장 가까우며 나머지 두 단어가 1글자 이상이도록 만들기
# 두번째 글자들 중 가장 작은 수를 맨 앞으로 바꾸기
# 세번째 글자들 중 가작 작은 수를 맨 앞으로 바꾸기
# WORD = list("mobitel")
# new_list = WORD
# one = new_list.index(min(new_list[:-2]))
# one_new_list = new_list[: one + 1]
# new_list = new_list[one + 1 :]
# one_new_list = one_new_list[::-1]  # 첫 번째 단어
# two = new_list.index(min(new_list[:-1]))
# two_new_list = new_list[one : two + 1]
# two_new_list = two_new_list[two::-1]
# print(two_new_list)
# one_new_list.extend(two_new_list[::-1])
# one_new_list.extend(new_list[::-1])
# print(one_new_list)substring not found
# print("".join(one_new_list))

# zzaa try, except로 해결
# aabc 반복문으로 해결
# abbc 반복문으로 해결
# 반복문으로 index다음의 밸류가 일치할 때까지?
# WORD = "mobitel"
# zyaa 미해결
WORD = input()
print(WORD[:-2].min(WORD))
try:
    FIRST_LEN = WORD[:-2].index(min(WORD))
    while WORD[FIRST_LEN] == WORD[FIRST_LEN + 1]:
        FIRST_LEN += 1
except ValueError:
    FIRST_LEN = 0
FIRST_WORD = WORD[: FIRST_LEN + 1]
WORD = WORD[FIRST_LEN + 1 :]
SECOND_LEN = WORD[:-1].index(min(WORD))
print(FIRST_WORD)
for i in range(len(WORD)):
    print(WORD[i])
    if WORD[i] != WORD[i + 1]:
        break
    SECOND_LEN += 1

SECOND_WORD = WORD[: SECOND_LEN + 1]
WORD = WORD[SECOND_LEN + 1 :]
print(FIRST_WORD[::-1] + SECOND_WORD[::-1] + WORD[::-1])
