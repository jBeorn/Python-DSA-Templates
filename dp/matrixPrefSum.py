# https://usaco.guide/silver/more-prefix-sums?lang=py
# https://leetcode.com/problems/range-sum-query-2d-immutable/

def buildPrefixMatrix(matrix):
    m, n = len(matrix), len(matrix[0])
    prefSumMatrix = [[0] * (n + 1) for _ in range(m + 1)]
    for r in range(m):
        for c in range(n):
            prefSumMatrix[r+1][c+1]=prefSumMatrix[r+1][c]+prefSumMatrix[r][c+1]-prefSumMatrix[r][c]+matrix[r][c]
    return prefSumMatrix

def sumRegion(prefSumMatrix, row1: int, col1: int, row2: int, col2: int) -> int:
    row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
    return prefSumMatrix[row2][col2] - prefSumMatrix[row2][col1 - 1] - prefSumMatrix[row1 - 1][col2] + prefSumMatrix[row1 - 1][col1 - 1]