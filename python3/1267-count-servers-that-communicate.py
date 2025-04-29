from typing import List
from collections import deque

def countServers(grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    count = 0

    # first pass, store number of servers in each row and column
    row_servers = [0] * m
    col_servers = [0] * n
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                row_servers[i] += 1
                col_servers[j] += 1
    
    # second pass, check if the server can communicate with other servers
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                if row_servers[i] > 1 or col_servers[j] > 1:
                    count += 1
    return count

print(countServers(grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]))