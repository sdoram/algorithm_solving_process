# https://www.acmicpc.net/problem/1924

# 2007년 1월 1일 월요일

day_of_the_week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
# 2월이 주어졌을 때 1월을 카운트 하기위해서는 인덱스 3이어야 하므로 1월이 2번 index에 위치하도록 조정
months = [0, 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month, day = map(int, input().split())
# month까지의 모든 개월 + 일수 더하기
days = sum(months[:month+1])+day
# 2007년 1월 1일 = 월요일 <= 0이면 일요일
# 7을 기준으로 나눈 나머지만 필요함
print(day_of_the_week[days % 7])
