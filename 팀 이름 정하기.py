# https://www.acmicpc.net/problem/1296

# name = 'JANE'
name = input()
# team_names = ['THOMAS',
#               'MICHAEL',
#               'INDY',
#               'LIU']
team_names = []
for _ in range(int(input())):
    team_names.append(input())
winner = {}
for team in team_names:
    L = name.count('L')+team.count('L')
    O = name.count('O')+team.count('O')
    V = name.count('V')+team.count('V')
    E = name.count('E')+team.count('E')
    per = (((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100)
    if per not in winner:
        winner[per] = [team]
    else:
        winner[per] += [team]
        # sorted(winner, reverse=True)[0] per가 가장 높은 key 가져오기
        # sorted(winner[key][0])로 가장 높은 key의 value를 사전순으로 정렬하고 [0]번 가져오기
print(sorted(winner[sorted(winner, reverse=True)[0]])[0])
