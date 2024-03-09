import collections


"""
BFS
O(V+E)
"""
grid = [[]]

isValid = lambda r, c : 0 <= r < len(grid) and 0 <= c < len(grid[0])

def bfs_AdjLst(start, adjLst):
    queue = collections.deque([start])
    seen = set([start])
    while queue:
        node = queue.popleft()
        for neig in adjLst[node]:
            if neig not in seen:
                seen.add(neig)
                queue.append(neig)


def bfsGrid_4way(start, grid):
    m, n = len(grid), len(grid[0])
    queue = collections.deque([start])
    seen = set([start])
    while queue:
        r, c = queue.popleft()
        for x, y in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):
            if 0 <= x < m and 0 <= y < n and (x,y) not in seen:
                seen.add((x,y))
                queue.append((x,y))


def bfsGrid_8way(start, grid):
    m, n = len(grid), len(grid[0])
    queue = collections.deque([start])
    seen = set([start])
    while queue:
        r, c = queue.popleft()
        for x, y in (r, c+1),(r+1, c+1),(r+1, c),(r+1, c-1),(r, c-1),(r-1, c-1),(r-1, c),(r-1, c+1):
            if 0 <= x < m and 0 <= y < n and (x,y) not in seen:
                seen.add((x,y))
                queue.append((x,y))


def bfsGrid2(start, grid):
    queue = collections.deque([start])
    seen = set([start])
    while queue:
        r, c = queue.popleft()
        for xx, yy in (-1, 0), (1, 0), (0, -1), (0, 1):
            x, y = r + xx, c + yy
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and (x,y) not in seen:
                seen.add((x,y))
                queue.append((x,y))