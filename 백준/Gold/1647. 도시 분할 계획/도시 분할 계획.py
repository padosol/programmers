N, M = map(int, input().split())
node = []
for _ in range(M):
    node.append(list(map(int, input().split())))

node.sort(key=lambda x: x[2])

p = [i for i in range(N + 1)]
def find(a):
    if a != p[a]:
        p[a] = find(p[a])
    return p[a]

def union(a, b):
    pa = find(a)
    pb = find(b)
    p[pa] = pb


ans = 0
ans_max = 0
for a,b,c in node:
    if find(a) != find(b):
        union(a, b)
        ans += c
        if ans_max < c:
            ans_max = c

print(ans-ans_max)
