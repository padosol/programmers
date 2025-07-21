T = int(input())

def find(a):
    if a != network[a][0]:
        network[a] = find(network[a][0])
    return network[a]

def union(a, b):
    if a not in network:
        network[a] = [a, 1]

    if b not in network:
        network[b] = [b, 1]

    a, pa = find(a)
    b, pb = find(b)
    if a != b:
        network[a] = network[b] = [a, pa + pb]

    return network[a][1]


for _ in range(T):
    F = int(input())

    network = {}
    for _ in range(F):
        a, b = input().split()
        print(union(a, b))