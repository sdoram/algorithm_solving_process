def solution(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i][j] != arr[j][i]:
                return 0
    return 1


print(solution([[0]*1000 for _ in range(1000)]))
# 0.1383202075958252초


def solution(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != arr[j][i]:
                return 0
    return 1


print(solution([[0]*1000 for _ in range(1000)]))
# 0.23602867126464844초
