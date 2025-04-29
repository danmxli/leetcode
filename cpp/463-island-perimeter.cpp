#include <vector>
#include <iostream>
#include <queue>
using namespace std;

class Solution
{
public:
    int islandPerimeter(vector<vector<int>> &grid)
    {
        int rows = grid.size();
        int cols = grid[0].size();
        int perimeter = 0;
        queue<pair<int, int>> q;
        vector<vector<bool>> visited(rows, vector<bool>(cols, false));
        vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < cols; j++)
            {
                if (grid[i][j] == 1)
                {
                    q.push({i, j});
                    visited[i][j] = true;
                    while (!q.empty())
                    {
                        auto cell = q.front();
                        q.pop();
                        int x = cell.first;
                        int y = cell.second;
                        for (int k = 0; k < 4; k++)
                        {
                            int adj_x = x + directions[k].first;
                            int adj_y = y + directions[k].second;
                            if ((0 > adj_x || adj_x >= rows) || (0 > adj_y || adj_y >= cols))
                            {
                                perimeter++;
                            }
                            else if (grid[adj_x][adj_y] == 0)
                            {
                                perimeter++;
                            }
                            else if (!visited[adj_x][adj_y])
                            {
                                visited[adj_x][adj_y] = true;
                                q.push({adj_x, adj_y});
                            }
                        }
                    }
                    return perimeter;
                }
            }
        }
        return perimeter;
    }
};

int main()
{
    Solution solution;
    vector<vector<int>> grid = {{1, 0}};
    cout << solution.islandPerimeter(grid) << endl;
    return 0;
}