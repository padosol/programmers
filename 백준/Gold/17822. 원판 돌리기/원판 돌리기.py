from collections import deque

N, M, T = map(int, input().split())
circle = [deque() for _ in range(N)]

for i in range(N):
    circle[i] = deque(list(map(int, input().split())))

numbers = [list(map(int, input().split())) for _ in range(T)]

def addSet(remove_list, i, j):
    if circle[i][j] != 0:
        remove_list.add(tuple([i, j]))

for t in range(T):
    x, d, k = numbers[t]

    for idx, c in enumerate(circle):
        if (idx + 1) % x == 0:
            if d == 0:
                c.rotate(k)
            else:
                c.rotate(-k)

    remove_list = set()

    # 인접하면서 수가 같은 것을 모두 지움 ( 0 으로 만듬 )
    for i in range(N):
        for j in range(M):
            if j == 0:
                if circle[i][0] == circle[i][1] or circle[i][0] == circle[i][M-1]:
                    addSet(remove_list, i, j)
            elif j == M-1:
                if circle[i][M-1] == circle[i][0] or circle[i][M-1] == circle[i][M-2]:
                    addSet(remove_list, i, j)
            else:
                if circle[i][j] == circle[i][j-1] or circle[i][j] == circle[i][j+1]:
                    addSet(remove_list, i, j)

            if i == 0:
                if circle[0][j] == circle[1][j]:
                    addSet(remove_list, i, j)
            elif i == N-1:
                if circle[N-1][j] == circle[N-2][j]:
                    addSet(remove_list, i, j)
            else:
                if circle[i][j] == circle[i-1][j] or circle[i][j] == circle[i+1][j]:
                    addSet(remove_list, i, j)

    if bool(remove_list):
        for [i, j] in remove_list:
            circle[i][j] = 0
    else:
        total = 0
        count = 0
        for i in range(N):
            for j in range(M):
                if circle[i][j] != 0:
                    total += circle[i][j]
                    count += 1
                    
        if total == 0 or count == 0:
            break
            
        avg = total / count
        for i in range(N):
            for j in range(M):
                if circle[i][j] > avg :
                    circle[i][j] = circle[i][j] - 1
                elif 0 < circle[i][j] < avg:
                    circle[i][j] = circle[i][j] + 1


answer = 0
for i in range(N):
    for j in range(M):
        answer += circle[i][j]

print(answer)
