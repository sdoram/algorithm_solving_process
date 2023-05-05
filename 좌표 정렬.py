# https://www.acmicpc.net/problem/11650

# 테스트 케이스 T
# 점의 좌표 x,y
# x가 커지는 순서, x가 같으면 y가 커지는 순서
# x를 기준으로 sort하고 y를 기준으로sort?
dot_list = [[3, 4],
            [1, 1],
            [1, -1],
            [2, 2],
            [3, 3],
            [1, -2]]
# dot_list = []
# for _ in range(int(input())):
# dot_list.append(list(map(int, input().split())))
# sort를 하고 1차적으로 진행하고 y에 해당하는 1번 index를
# 따로 정렬해야 하는 줄 알았는데 [0][1]모두 숫자라 그런지 잘 정렬됐다.
for dot in sorted(dot_list):
    print(*dot)
