# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/181833

def solution(n):
    # n은 정수
    # return은 n*n의 이차원 배열
    # arr[i][j]의 값이 일치하는 부분의 원소는 1, 아니면 0
    # [[0]*n]*n으로 *연산자를 사용해 생성시 얕은 복사로 다른 원소 조작시 같은 인덱스의 원소 모두 변경
    # *로 만들면 [0]*n이라는 것을 *n만큼 똑같이 만들어내기 때문에 같은 id값을 가짐
    a = ([[0]*n]*n)  # *사용 시 얕은복사로 사용 불가
    two_dimensional_array = [[0]*n for i in range(n)]  # 가능
    test_array = [[0 for i in range(n)] for j in range(n)]  # 가능
    # 이차원 배열 확인
    print(a, '= a')
    print(two_dimensional_array, '= two_dimensional_array')
    print(test_array, '= test_array')
    print()
    # 모두 같은 id를 가짐
    print(f'a[0]의 id : {id(a[0])}')
    print(f'a[1]의 id : {id(a[1])}')
    print(f'a[2]의 id : {id(a[2])}')
    print()
    # 모두 다른 id를 가짐
    print(f'two_dimensional_array[0]의 id : {id(two_dimensional_array[0])}')
    print(f'two_dimensional_array[1]의 id : {id(two_dimensional_array[1])}')
    print(f'two_dimensional_array[2]의 id : {id(two_dimensional_array[2])}')
    print()
    # 모두 다른 id를 가짐
    print(f'test_array[0]의 id : {id(test_array[0])}')
    print(f'test_array[1]의 id : {id(test_array[1])}')
    print(f'test_array[2]의 id : {id(test_array[2])}')
    # enumerate 사용시 순서(기본값=0), for문 내용으로 두 개의 인자 사용
    # enumerate(for문 대상, 시작값=생략가능)
    # 0부터, 리스트i
    for j, i in enumerate(two_dimensional_array):
        print(f'변경전 값 {i, j}')
        i[j] = 1
        print(f'변경후 값 {i, j}')
        print()

    # 2중 for문
    for i in range(n):
        for j in range(n):
            print(j, i)
            if i == j:
                test_array[i][j] = 1
    print(test_array)
    return two_dimensional_array


print(solution(3))
