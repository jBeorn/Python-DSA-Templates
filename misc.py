
abcLowercaseString = "".join([chr(i + ord("a")) for i in range(26)])

def isInLine(a, b, c):
        return ((b[0] - a[0])*(c[1] - a[1]) - (b[1] - a[1])*(c[0] - a[0]))