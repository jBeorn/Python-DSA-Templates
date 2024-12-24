import collections


def toposort(adjLst, n):
    inDegree = [0] * n
    for neighbours in adjLst:
        for neig in neighbours:
            inDegree[neig] += 1
    queue = collections.deque([])
    for node in range(n):
        if inDegree[node] == 0:
            queue.append(node)
    visited = 0
    order = []
    while queue:
        node = queue.popleft()
        visited += 1
        order.append(node)
        for nxt in adjLst[node]:
            inDegree[nxt] -= 1
            if inDegree[nxt] == 0:
                queue.append(nxt)
    return order