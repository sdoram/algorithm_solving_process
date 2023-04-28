def solution(n):
    answer = []
    i = 2
    # n == i이면 소수 or 모두 분해한 경우
    while n >= i:
        # 소인수 찾기
        if n % i == 0:
            # n값 변경
            n = n//i
            # answer에 추가
            answer.append(i)
            # 다시 2부터 시작
            continue
        i += 1
    answer = list(set(answer))
    print(answer)  # set일 때 정렬이 안된 값
    answer.sort()
    print(answer)  # sort로 정렬
    return answer


print(solution(420123))
