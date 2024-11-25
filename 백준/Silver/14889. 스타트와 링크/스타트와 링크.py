def team_cal():
    team_a = 0
    team_b = 0

    for i in range(N):
        for j in range(i+1, N):
            if team[i] and team[j]:
                team_a += (team_score[i][j] + team_score[j][i])
            elif not team[i] and not team[j]:
                team_b += (team_score[i][j] + team_score[j][i])

    return abs(team_a - team_b)


def recur(len, idx):
    global answer
    if len * 2 == N:
        answer = min(answer, team_cal())
        return

    for i in range(idx, N):
        team[i] = True
        recur(len + 1, i+1)
        team[i] = False


N = int(input())
team = [False for _ in range(N)]
team_score = [list(map(int, input().split())) for _ in range(N)]

answer = 2000

team[0] = True
recur(1, 1)

print(answer)
