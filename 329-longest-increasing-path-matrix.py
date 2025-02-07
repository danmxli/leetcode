from typing import List

# intuition:
# 1. use dfs to find the longest increasing path
# 2. use memoization to store the longest increasing path for each cell
# 3. use a visited set to avoid revisiting the same cell
# 4. use a direction array to traverse the matrix

def longestIncreasingPath(matrix: List[List[int]]) -> int:
    if not matrix or not matrix[0]:
        return 0
    
    m = len(matrix)
    n = len(matrix[0])
    memo = [[0] * n for _ in range(m)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    def dfs(x, y):
        if memo[x][y] != 0:
            return memo[x][y]
        
        memo[x][y] = 1
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] > matrix[x][y]:
                memo[x][y] = max(memo[x][y], 1 + dfs(nx, ny))
        return memo[x][y]
    
    return max(dfs(i, j) for i in range(m) for j in range(n))

if __name__ == "__main__":
    matrix = [[9,9,4],[6,6,8],[2,1,1]]
    print(longestIncreasingPath(matrix))
