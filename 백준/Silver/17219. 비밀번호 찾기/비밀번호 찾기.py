n, m = map(int, input().split())
domain = {}
for _ in range(n):
    d, p = input().split()
    domain[d] = p

for _ in range(m):
    d = input()
    print(domain[d])