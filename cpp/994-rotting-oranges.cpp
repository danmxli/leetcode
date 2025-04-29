#include <vector>
#include <iostream>
#include <queue>
#include <print>
using namespace std;

class Solution
{
public:
    int orangesRotting(vector<vector<int>> &grid)
    {
        int m = grid.size();
        int n = grid[0].size();
        queue<pair<int, int>> q;
        vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        int time = -1;
        int fresh_count = 0;
        // vector<vector<bool>> visited(m, vector<bool>(n, false));

        // first pass to find all the initial rotting oranges
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (grid[i][j] == 2)
                {
                    q.push({i, j});
                }
                else if (grid[i][j] == 1)
                {
                    fresh_count++;
                }
            }
        }

        if (!fresh_count)
        {
            return 0;
        }

        while (!q.empty())
        {
            time++;
            int l = q.size();
            for (int i = 0; i < l; i++)
            {
                auto cell = q.front();
                q.pop();
                for (int j = 0; j < 4; j++)
                {
                    int adj_m = cell.first + directions[j].first;
                    int adj_n = cell.second + directions[j].second;
                    if (0 > adj_m || adj_m >= m || 0 > adj_n || adj_n >= n)
                    {
                        continue;
                    }
                    if (grid[adj_m][adj_n] == 2 || grid[adj_m][adj_n] == 0)
                    {
                        continue;
                    }
                    grid[adj_m][adj_n] = 2;
                    q.push({adj_m, adj_n});
                    fresh_count--;
                }
            }
        }

        if (fresh_count)
        {
            return -1;
        }
        return time;
    }
};

int main()
{
    Solution solution;
    // vector<vector<int>> grid = {{2, 1, 1}, {1, 1, 0}, {0, 1, 1}};
    // vector<vector<int>> grid = {{2, 1, 1}, {0, 1, 1}, {1, 0, 1}};
    vector<vector<int>> grid = {{2, 1, 1}, {1, 1, 1}, {0, 1, 2}};
    cout << solution.orangesRotting(grid) << endl;
    return 0;
}