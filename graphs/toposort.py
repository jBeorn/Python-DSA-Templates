import collections


def toposort(adjLst, n):
    inDegree = [0] * n
    for neighbours in adjLst:
        for neig in neighbours:
            inDegree[neig] += 1
    queue = collections.deque([])
    for course in range(n):
        if inDegree[course] == 0:
            queue.append(course)
    coursesTaken = 0
    order = []
    while queue:
        node = queue.popleft()
        coursesTaken += 1
        order.append(node)
        for next in adjLst[node]:
            inDegree[next] -= 1
            if inDegree[next] == 0:
                queue.append(next)
    return order