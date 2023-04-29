# https://www.acmicpc.net/problem/10815
import sys
import time
start_time = time.time()  # 측정 시작
# 입력
# N = 내 숫자 카드 N개
# N개의 숫자
# M = 비교할 숫자 M개
# M개의 숫자
# 출력 M개의 숫자가 각각 내 숫자 카드에 속하는지 확인하고 1 or 0 출력

N = int(sys.stdin.readline())
N_list = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))
N_list = set(N_list)

answer_list = [1 if m in N_list else 0 for m in M_list]
print(*answer_list)


# 프로그램 소스코드
end_time = time.time()  # 측정 종료
print("time:", end_time - start_time)  # 수행 시간 출력

# list의 in은 O(n)의 시간복잡도
# set의 in은 O(1)의 시간복잡도를 가진다.
# set의 O(1)인 이유는 입력 순서대로 index를 가지는 게 아닌 입력 값에 따라서
# 해시 테이블(hash table) <= drf 비밀번호 해시랑 같은 구조?
# 해시 값에 따라 index가 정해지므로 in함수가 1개만 확인하고 존재 여부를 판단할 수 있다.
# 아마 이전에 set으로 중복값을 제거 했을 때 다시 list로 변환하는 과정에서 기존 list index가 아닌
# 가끔씩 튀는 숫자가 있던게 오늘 알게된 해시 테이블로 index 순서가 바뀌는 과정이 있던 것 같다.
