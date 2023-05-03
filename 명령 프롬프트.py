# https://www.acmicpc.net/problem/1032

# a?b의 경우 a로 [?] b로 끝나는 문자

# 입력 테스트 개수
# 입력 테스트 코드
# 출력은 ?를 최소한으로 사용한 결과

for _ in range(int(input())):
    test_code = input()
    # 첫번째 입력 값으로 초기값 설정
    if _ == 0:
        answer = list(test_code)
    # 초기값과 현재 매개변수가 다르면 ?로 변환
    for i, t in enumerate(test_code):
        if answer[i] != t:
            answer[i] = '?'
print(''.join(answer))
