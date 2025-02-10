from typing import List

def findMaxFish(grid: List[List[int]]) -> int:
    ...
    M = len(grid)
    N = len(grid[0])

    def dfs(i,j):
        ...
        # base case
        if not(0 <= i < M) or not(0 <= j < N) or grid[i][j] == 0:
            return 0
        
        # floodfill
        curr = grid[i][j]
        grid[i][j] = 0
        count = curr + dfs(i-1,j) + dfs(i+1,j) + dfs(i,j-1) + dfs(i,j+1)
        return count

    # driver
    answer = 0
    for i in range(M):
        for j in range(N):
            if grid[i][j] != 0:
                answer = max(answer, dfs(i,j))

    return answer

print(findMaxFish(grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]))