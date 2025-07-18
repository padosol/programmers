import sys
sys.setrecursionlimit(10**6)
V, E = map(int, input().split())

tree = []
for i in range(E):
    tree.append(list(map(int, input().split())))

tree.sort(key=lambda x: x[2])

parent = list(range(V+1))
def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

ans = 0
for a, b, c in tree:
    if find(a) != find(b):
        union(a, b)
        ans += c

print(ans)