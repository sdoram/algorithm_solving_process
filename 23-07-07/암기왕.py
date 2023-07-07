# https://www.acmicpc.net/problem/2776

# 최초 작성 코드
# from sys import stdin

# for _ in range(int(stdin.readline())):
#     N = int(stdin.readline())
#     N_word = {i: True for i in list(map(int, stdin.readline().split()))}
#     M = int(stdin.readline())
#     M_word = list(map(int, stdin.readline().split()))
#     for m in M_word:
#         print(int(N_word.get(m, False)))

# 최종 개선 버전
# 입력이 1,000,000개까지 들어올 수 있으므로 빠른 입출력 사용
from sys import stdin

for _ in range(int(stdin.readline())):
    N = int(stdin.readline())
    # dictionary comprehension을 통한 dict 선언
    N_word = {i: "1" for i in list(map(int, stdin.readline().split()))}
    M = int(stdin.readline())
    M_word = list(map(int, stdin.readline().split()))
    # N_word.get(m, "0") n_word라는 dict에 m이라는 key가 존재하면 그 value를 가져오고,
    # 없을 경우 m을 key로 하는 "0"의 value를 생성
    # join을 사용하기 위한 형변환 과정을 최소화 하기 위해 int, boolean 대신 str로 value설정
    print("\n".join([N_word.get(m, "0") for m in M_word]))
