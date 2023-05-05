# https://www.acmicpc.net/problem/10814


# 문자열로 key를 받으면 정렬이 첫 글자를 기준으로 정렬해서
# key값의 범위가 넓어지면 정렬에서 문제 생김

# key가 str인 경우
# members = {'100': ['junkyu', 'dohyun'],
#    '2': ['sunyonug']}
# key가 int인 경우
# members = {100: ['junkyu', 'dohyun'],
#    20: ['sunyonug']}
members = {}
for _ in range(int(input())):
    age, name = input().split()
    age = int(age)
    if age not in members:
        members[age] = [name]
    else:
        members[age] += [name]
# key를 기준으로 오름차순 정렬 == 나이순 정렬
sorted_members = sorted(members)
for age in sorted_members:
    # 같은 나이의 회원이 여럿일 경우 for문 반복
    for name in members[age]:
        print(age, name)
