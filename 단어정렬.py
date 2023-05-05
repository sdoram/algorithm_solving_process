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
