# https://school.programmers.co.kr/learn/courses/30/lessons/120866
# 8개의 칸을 위험 지역으로 바꾸기
# -1이 되거나 길이를 벗어나는 경우 컨트롤

def solution(board):
    # 얕은 복사를 방지하기 위해서 for문을 사용한 이차원 배열 만들기
    new_board = [[0]*len(board) for _ in board]
    # index의 위치를 알기 위한 enumerate사용
    for i1, b1 in enumerate(board):
        for i2, b2 in enumerate(b1):
            # 폭탄이 있으면
            if b2 == 1:
                # 상하 index를 range로 표현
                for n1 in range(i1-1, i1+2):
                    # 이차원 배열 범위 밖으로 나가는 경우 방지
                    if len(board) > n1 >= 0:
                        # 좌우 index를 range로 표현
                        for n2 in range(i2-1, i2+2):
                            # 이차원 배열 범위 밖으로 나가는 경우 방지
                            if len(board) > n2 >= 0:
                                # print(n1, n2) # 위험한 지역
                                new_board[n1][n2] = 1
    print(new_board)
    # len(board)**2로 이차원 배열의 총 원소 개수 구하기
    # [sum(n) for n in new_board]으로 각 리스트별 안전하지 않은 장소 숫자 리스트로 구하기
    # sum()으로 안전하지 않은 장소 총합 구하기
    return len(board)**2-sum([sum(n) for n in new_board])


print(solution([[1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [
      0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]))
