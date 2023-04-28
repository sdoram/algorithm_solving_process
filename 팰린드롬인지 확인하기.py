# 입력은 알파벳 소문자로 이루어진 단어
# 팰린드롬인지 확인하기 <= 앞으로 읽는 것과 거꾸로 읽을 때 동일한 단어
# level, noon은 팰린드롬, baekjoon은 팰린드롬이 아니다.
# 출력 입력이 팰린드롬이면 1 아니면 0

# word_input = input()
# word_input = 'level'

# word_input과 word_input[::-1]이 동일한지 판단


def palindrome(word):
    for idx1, w in enumerate(word):
        for idx2, reverse_w in enumerate(word[::-1]):
            if idx1 == idx2:
                if w != reverse_w:
                    return 0
    return 1


print(palindrome(input()))
