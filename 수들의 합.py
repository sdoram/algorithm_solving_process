# https://www.acmicpc.net/problem/1789

# 서로 다른 N개의 자연수의 합 S
# S가 주어질 때, N의 최댓값 구하기
# S = 200일 때 N = 19
# for문으로 1부터 S가 초과하는 타이밍까지 계산하고 그 전의 수까지 빼버림
# 그리고 S - 이제까지 더한 숫자를 하면 마지막 숫자 확인 가능
# S = 200
S = int(input())
num = 0
count = 1
while True:
    num += count
    # S가 200일 때 190 + 19를 하면 초과 하므로 19대신 200을 채웠다는 가정
    if num + count+1 > S:
        print(count)
        break
    count += 1

# 리스트로 값 확인하기
S = 200
num = 0
num_list = []
count = 1
while True:
    num += count
    num_list.append(count)
    # S가 200일 때 190 + 19를 하면 초과 하므로 19대신 200을 채웠다는 가정
    if num + count+1 > S:
        print(count)
        # 불가능해지는 숫자 제거
        num_list.pop()
        # 불가능해진 숫자 + 남은 숫자 더한 값 리스트에 추가
        num_list.append(S-(num-count))
        break
    count += 1
print(num_list)
print(sum(num_list))
