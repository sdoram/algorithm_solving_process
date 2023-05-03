# https://www.acmicpc.net/problem/1100

# 체스판 8*8, 0,0은 하얀색
# 체스판을 무식하게 이차원 배열로 만들었다.
white = [[0, 1, 0, 1, 0, 1, 0, 1],
         [1, 0, 1, 0, 1, 0, 1, 0],
         [0, 1, 0, 1, 0, 1, 0, 1],
         [1, 0, 1, 0, 1, 0, 1, 0],
         [0, 1, 0, 1, 0, 1, 0, 1],
         [1, 0, 1, 0, 1, 0, 1, 0],
         [0, 1, 0, 1, 0, 1, 0, 1],
         [1, 0, 1, 0, 1, 0, 1, 0]]
# 테스트 코드
# chess_pieces = [
#     ['.', 'F', '.', 'F', '.', '.', '.', 'F'],
#     ['F', '.', '.', '.', 'F', '.', 'F', '.'],
#     ['.', '.', '.', 'F', '.', 'F', '.', 'F'],
#     ['F', '.', 'F', '.', '.', '.', 'F', '.'],
#     ['.', 'F', '.', '.', '.', 'F', '.', '.'],
#     ['F', '.', '.', '.', 'F', '.', 'F', '.'],
#     ['.', 'F', '.', 'F', '.', 'F', '.', 'F'],
#     ['.', '.', 'F', 'F', '.', '.', 'F', '.'],
# ]
count = 0
chess_pieces = []
# 말의 위치 입력받기
for _ in range(8):
    chess_piece = input()
    chess_pieces.append(chess_piece)

for idx, chess in enumerate(chess_pieces):
    for i, c in enumerate(chess):
        # 말이 존재하고 and 하얀색 칸에 있다면
        if c == 'F' and white[idx][i] == 0:
            count += 1
print(count)
