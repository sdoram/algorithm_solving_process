# https://school.programmers.co.kr/learn/courses/30/lessons/120911
def solution(my_string):
    # my_string = str
    # return 전부 소문자로 바꾸고, 알파벳 순서로 정렬
    # lower
    # .sort()
    answer = ''
    answer_list = [s for s in my_string.lower()]
    for str_ in my_string:
        answer_list.append(str_.lower())
    answer_list.sort()

    answer = ''.join(answer_list)
    # .join이나 for문 사용
    # for ans in answer_list:
    # answer += ans
    return answer


def solution(my_string):
    answer_list = [s for s in my_string.lower()]
    answer_list.sort()
    return ''.join(sorted(answer_list))


def solution(my_string):
    answer_list = sorted([s for s in my_string.lower()])
    return ''.join(sorted(answer_list))


def solution(my_string):
    return ''.join(sorted([s for s in my_string.lower()]))
