# https://school.programmers.co.kr/learn/courses/30/lessons/120896
def solution(s):
    # 문자열 s
    # in으로 확인하기
    answer = ''
    s_list = {}
    for i in s:
        if i not in s_list:
            s_list[i] = 1
        elif i in s_list:
            s_list[i] += 1
    # for문의 순서 = key를 기준으로 sort된 s_list로 사용
    for i in sorted(s_list.keys()):
        # value 값이 1이면
        if s_list[i] == 1:
            answer += i
    return answer


def solution(s):
    s_dict = {}
    for i in s:
        # s_dict에 없다면
        if i not in s_dict:
            s_dict[i] = 1
        # s_dict에 있다면
        elif i in s_dict:
            s_dict[i] += 1
        # if 값이 1인 key를 정렬해서 리스트화
        # ''.join()으로 리스트 언패킹
    return ''.join([i for i in sorted(s_dict.keys()) if s_dict[i] == 1])


def solution(s):
    answer = []
    pop_list = []
    for i in s:
        # answer에 i가 없다면
        if i not in answer:
            answer.append(i)
        # answer에 i가 있다면
        else:
            pop_list.append(i)
    for p in set(pop_list):
        # 전체 리스트에서 index찾기
        pop_index = answer.index(p)
        # 전체 리스트에서 빼기
        answer.pop(pop_index)
        # del로 같은 결과 가능
        # del answer[pop_index]
    return ''.join(sorted(answer))

# index로 찾기
# index가 2번째 값을 찾으면 패스


def solution(s):
    answer = ''
    for n in set(s):
        # 첫번째 index 찾기
        first_index = s.index(n)
        # 두번째 index 찾기 시도
        try:
            _ = s.index(n, first_index+1)
        # 두번째 index가 없을 경우 except ValueError:
        except ValueError:
            answer += n
    return ''.join(sorted(answer))


print(solution("abcabcadc"))
# print(solution("hello"))


def solution(s):
    # 이건 생각 못했다. count 함수는 알고 있지만 써야겠다는 생각이 잘 안든다.
    # for문 = set()으로 중복을 제거하고 sorted()로 정렬된 s
    # i = count로 확인된 숫자가 1개인 변수
    return ''.join([i for i in sorted(set(s)) if s.count(i) == 1])


# print(solution("abcabcadc"))
# print(solution("abdc"))
