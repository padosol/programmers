from collections import deque
def solution(n, m, x, y, r, c, k):
    answer = 'impossible'
    # 문자열 순이니깐 방향을 문자열 순서로 움직이면 됨
    # 0 < x <= n, 0 < y <= m
    # d 아래, l 왼쪽, r 오른쪽 u 위
    d = [(1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r'), (-1, 0, 'u')]
    q = deque()
    q.append((x,y,'', 0))

    while q:
        sx, sy, value, cnt = q.popleft()

        # 도착했는데 남은 거리가 홀수라면 도착지에 k만큼 오지 못한다!
        if (sx, sy) == (r, c) and (k - cnt) % 2:
            return 'impossible'
        elif (sx, sy) == (r, c) and cnt == k:
            return value

        for i in range(4):
            nsx = sx + d[i][0]
            nsy = sy + d[i][1]
            nv = value + d[i][2]
            n_cnt = cnt + 1

            if 0 < nsx <= n and 0 < nsy <= m:
                if abs(nsx - r) + abs(nsy - c) + n_cnt > k:
                    continue
                q.append((nsx, nsy, nv, n_cnt))
                break

    return answer