# https://school.programmers.co.kr/learn/courses/30/lessons/12940
# 다른 사람의 풀이 보면서 공부하기
import math


def solution(n, m):
    # 이전에 알게된 math의 최대공약수 함수 gcd 사용
    # 최소 공배수를 뜻하는 lcm은 프로그래머스 환경에서 사용 불가
    return [math.gcd(n, m), n * m // math.gcd(n, m)]
