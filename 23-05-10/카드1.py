# https://www.acmicpc.net/problem/2161

# 가장 위의 index pop
# 그 다음 index 맨 뒤로 보내기
N = int(input())
card_list = [n for n in range(1,N+1)]
drop_card_list = []
while True:
    drop_card_list.append(card_list.pop(0))
    try:
        # card_list == []이면 IndexError발생
        card_list.append(card_list.pop(0))
    except IndexError:
        print(*drop_card_list)
        break
