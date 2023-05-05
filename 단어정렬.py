# https://www.acmicpc.net/problem/1181
# set으로 중복 날리기

word_dict = {
    3: ['but'],
    1: ['i'],
    8: ['hesitate'],
    2: ['no', 'it', 'im', 'no'],
    4: ['more', 'wait', 'more', 'wont'],
    6: ['cannot'],
    5: ['yours'],
}
word_dict = {}
# 테스트 케이스만큼 입력 받기
for _ in range(int(input())):
    word = input()
    # key가 문자열의 길이 value가 단어로 딕셔너리 넣기
    if len(word) not in word_dict:
        word_dict[len(word)] = [word]
    else:
        word_dict[len(word)] += [word]
# key를 기준으로 정렬
for num in sorted(word_dict):
    # 밸류를 set으로 중복 제거, sorted로 사전순 정렬
    for word in sorted(set(word_dict[num])):
        print(word)

word_dict = {
    'but': 3,
    'i': 1,
    'wont': 4,
    'hesitate': 8,
    'no': 2,
    'more': 4,
    'it': 2,
    'cannot': 6,
    'wait': 4,
    'im': 2,
    'yours': 5
}

word_dict = {}
# 테스트 케이스만큼 입력 받기
for _ in range(int(input())):
    word = input()
    # key가 문자, value가 단어의 길이로 딕셔너리 넣기
    # 중복인 경우 겹치므로 중복 제거 필요 X
    if word not in word_dict:
        word_dict[word] = [len(word)]
# word를 사전순으로 먼저 정렬
word_dict = sorted(word_dict.items())
# 길이를 기준으로 재정렬
word_dict = sorted(word_dict, key=lambda value: value[1])
for word in word_dict:
    print(word[0])
