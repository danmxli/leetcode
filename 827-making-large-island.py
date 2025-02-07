from typing import List

def largestIsland(grid: List[List[int]]) -> int:
    N = len(grid)
    M = len(grid[0])

    # dfs to find the area of an island
    def dfs(i, j, id):
        if not(0 <= i < N) or not(0 <= j < M) or grid[i][j] != 1:
            return 0
        
        # mark the cell as visited with the id
        grid[i][j] = id
        count = 1 + dfs(i+1, j, id) + dfs(i-1, j, id) + dfs(i, j+1, id) + dfs(i, j-1, id)
        return count

    # 1st pass
    island_map = {}
    id = 2
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:
                area = dfs(i, j, id)
                island_map[id] = area
                id += 1

    # # # logging
    # print(grid)
    # print(island_map)

    # if there is one island
    if len(island_map) == 1:
        # if the grid is all 1s, return the area of the grid
        if sum(island_map.values()) == N * M:
            return N * M
        else:
            return island_map[2] + 1

    # 2nd pass
    max_area = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 0:
                # maintain a set of visited island ids
                visited_islands = set()

                # check the area of the island if we flip this cell
                curr_area = 1
                for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    adj_i = i + d[0]
                    adj_j = j + d[1]

                    if not(0 <= adj_i < N) or not(0 <= adj_j < M):
                        continue
                    
                    # check if the adjacent cell is an island
                    if grid[adj_i][adj_j] in island_map and grid[adj_i][adj_j] not in visited_islands:
                        curr_area += island_map[grid[adj_i][adj_j]]
                        visited_islands.add(grid[adj_i][adj_j])
                max_area = max(max_area, curr_area)

    return max_area

print(largestIsland(grid = [[0,0],[0,1]]))
print(largestIsland(grid = [[1,1],[1,1]]))