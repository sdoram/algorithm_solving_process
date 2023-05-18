# https://school.programmers.co.kr/learn/courses/30/lessons/17681


def solution(n, arr1, arr2):
    # 지도는 한 변의 길이가 n인 정사각형
    # 벽은 공백 or #으로 이루어짐
    # 지도1과 2를 겹쳐서 하나라도 벽이면 전체 지도에서 벽
    # arr = 0은 공백, 1은 벽으로 표현된 이진수를 10진수로 변환한 값

    # 각각의 arr의 원소를 2진수로 변환하기
    # arr1과 arr2가 아무나 1이라면 1 아니라면 0
    # 채우기
    answer = []
    for i in range(n):
        # arr1과 arr2의 합에 빈공간 0으로 채우기
        bin_ar = f"{int(bin(arr1[i])[2:]) + int(bin(arr2[i])[2:]):0>{n}}"
        # 0이면 공백, 1이나 2면 #으로 변환
        bin_ar = bin_ar.replace("0", " ").replace("1", "#").replace("2", "#")
        answer.append(bin_ar)
    return answer
