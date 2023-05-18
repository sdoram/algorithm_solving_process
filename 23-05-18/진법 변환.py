# https://www.acmicpc.net/problem/2745
N, B = "ZZZZZ", "36"
N, B = "A0", "20"
N, B = input().split()
B = int(B)
ANSWER = 0
# [::-1]로 일의 자리부터 시작
for idx, num in enumerate(N[::-1]):
    # 'A'~'Z'가 65부터 90이므로 if문 설정
    if 64 < ord(num) < 91:
        # pow(B,idx)로 몇 진수인지 파악
        ANSWER += (ord(num) - 55) * pow(B, idx)
    else:
        ANSWER += int(num) * pow(B, idx)
print(ANSWER)
