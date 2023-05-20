# https://www.acmicpc.net/problem/9506
# 주어진 수가 모든 약수들의 합과 같은지 파악하기

while True:
    n = int(input())
    if n == -1:
        break
    num_list = [num for num in range(1, (n - 1) // 2 + 2) if n % num == 0]
    if n == sum(num_list):
        # join이 str형일 때 사용 가능하므로 map과 조합해서 형변환
        print(f"{n} = {' + '.join(map(str, num_list))}")
    else:
        print(f"{n} is NOT perfect.")
