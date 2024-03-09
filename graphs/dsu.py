

def UnionFind():
    # def find(x):
    #     while x != parents[x]:
    #         x = parents[x]
    #     return x
    def find(x):
        # path compression
        if x == parents[x]:
            return x
        parents[x] = find(parents[x])
        return parents[x]
    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            if size[rootX] >= size[rootY]:
                parents[rootY] = rootX
                size[rootX] += size[rootY]
            else:
                parents[rootX] = rootY
                size[rootY] += size[rootX]
    parents = {}
    size = {}