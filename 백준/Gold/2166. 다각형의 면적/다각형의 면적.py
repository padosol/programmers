N = int(input())
points = []
for i in range(N):
    x, y = map(int, input().split())
    points.append([x, y])

sum_point1 = 0
sum_point2 = 0
for i in range(N):
    if i == N-1:
        sum_point1 += points[i][0] * points[0][1]
        sum_point2 += points[i][1] * points[0][0]
    else:
        sum_point1 += points[i][0] * points[i+1][1]
        sum_point2 += points[i][1] * points[i+1][0]

print(0.5 * (abs(sum_point1 - sum_point2)))
