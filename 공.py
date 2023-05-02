# https://www.acmicpc.net/problem/1547

# 컵이 세개 주어지고
# 공은 1번 위치 고정
# 컵의 위치를 M번 바꾼 뒤
# 공이 있는 위치 찾기
# 공이 사라진 경우 -1? <= 신경 쓸 필요 X
# 공을 M번 바꾼 후 1번 자리에 있는 숫자 출력하기
import sys
M = int(sys.stdin.readline())
cups = [1, 2, 3]
for _ in range(M):
    X, Y = map(int, sys.stdin.readline().split())
    X_location = cups.index(X)
    Y_location = cups.index(Y)
    # python의 한줄씩 실행하는 인터프리터의 특징상 가능한 코드
    cups[X_location], cups[Y_location] = cups[Y_location], cups[X_location]
print(cups[0])
