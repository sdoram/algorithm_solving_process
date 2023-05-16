# https://school.programmers.co.kr/learn/courses/30/lessons/77884
def solution(left, right):
    return sum(
        [
            num if int(num**0.5) != num**0.5 else -num
            for num in range(left, right + 1)
        ]
    )


# return sum([num if int(num**0.5) != num**0.5 else -num for num in range(left, right + 1)])
