# https://www.acmicpc.net/problem/1075
# 입력 정수 N과 F
N = int(input())
F = int(input())
# N = 32442
# F = 99
for n in range(100):
    # N//100으로 뒤의 두자리 0만들기 * 100으로 자리수 복구
    # %F == 0으로 나눠지는지 확인
    if (N//100*100+n) % F == 0:
        if n < 10:
            print('0'+str(n))
        else:
            print(str(n))
        break
