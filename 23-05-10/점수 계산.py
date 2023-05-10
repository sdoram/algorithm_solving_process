# https://www.acmicpc.net/problem/2822

# 8개의 입력중 높은 숫자 5개 

# 출력 총점
# 포함되는 문제 번호 
score_list = [[int(input()),num] for num in range(1,9)]
five_scores = sorted(score_list, reverse=True)[:5]
print(sum([score[0] for score in five_scores]))
print(*sorted([score[1] for score in five_scores]))
