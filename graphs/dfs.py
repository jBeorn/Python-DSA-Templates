
"""
DFS
O(V+E)
"""
    
def dfs_AdjLst(start, adjLst):
    stack = [start]
    seen = set([start])
    while stack:
        node = stack.pop()
        for neig in adjLst[node]:
            if neig not in seen:
                seen.add(neig)
                stack.append(neig)