import sys
sys.setrecursionlimit(10**5)

def insert(parent, node):
    if parent[0][1] > node[1]:
        if parent[1]:
            insert(parent[1], node)
        else:
            parent[1] = [node, [], []]
    else:
        if parent[2]:
            insert(parent[2], node)
        else:
            parent[2] = [node, [], []]

def pre_order(node):
    path = [node[0][0]]
    if node[1]:
        path += pre_order(node[1])

    if node[2]:
        path += pre_order(node[2])

    return path

def post_order(node):
    path = []
    if node[1]:
        path += post_order(node[1])

    if node[2]:
        path += post_order(node[2])

    path.append(node[0][0])

    return path

def solution(nodeinfo):
    nodes = [(idx + 1, x, y) for idx, (x, y) in enumerate(nodeinfo)]
    nodes = sorted(nodes, key=lambda x: x[2] * -1)

    # node, left, right
    tree = [nodes[0], [], []]
    for node in nodes[1:]:
        insert(tree, node)

    pre = pre_order(tree)
    post = post_order(tree)


    return [pre, post]