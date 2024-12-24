
abcLowercaseString = "".join([chr(i + ord("a")) for i in range(26)])

manhattanDist = lambda x, y: abs(x[0] - y[0]) + abs(x[1] - y[1])

def isInLine(a, b, c):
        return ((b[0] - a[0])*(c[1] - a[1]) - (b[1] - a[1])*(c[0] - a[0]))

def isRectangle(coords):
    euclidianDistance = lambda p1, p2: (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
    d1 = euclidianDistance(coords[0], coords[1])  # Bottom-left to Bottom-right
    d2 = euclidianDistance(coords[0], coords[2])  # Bottom-left to Top-left
    d3 = euclidianDistance(coords[1], coords[3])  # Bottom-right to Top-right
    d4 = euclidianDistance(coords[2], coords[3])  # Top-left to Top-right
    diag1 = euclidianDistance(coords[0], coords[3])  # Bottom-left to Top-right
    diag2 = euclidianDistance(coords[1], coords[2])  # Bottom-right to Top-left
    return d1 == d4 and d2 == d3 and diag1 == diag2