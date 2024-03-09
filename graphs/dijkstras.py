import heapq


def dijkstras(n, adjLst, start, dest):
    """ 
    Dijkstra's algortihm finds the shortest path from node start
    to all other nodes in a directed weighted graph.
    O((V+E)logV)
    """
    pqueue = [(0, start)]
    costLst = [float("inf")] * n
    costLst[start] = 0
    while pqueue:
        pathCost, node = heapq.heappop(pqueue)
        if node == dest:
            break
        if pathCost > costLst[node]:
            continue
        for nei, cost in adjLst[node]:
            if costLst[nei] > pathCost + cost:
                costLst[nei] = pathCost + cost
                heapq.heappush(pqueue, (pathCost + cost, nei))
    return costLst