#include <iostream>
#include <print>
#include <vector>
#include <queue>
using namespace std;

class Solution
{
public:
    int getArea(int i, int j, int M, int N, vector<vector<int>> &grid)
    {
        // floodfill algorithm
        vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        queue<pair<int, int>> q;

        // init
        q.push({i, j});
        grid[i][j] = 0;
        int size = 0;

        while (!q.empty())
        {
            auto curr = q.front();
            q.pop();
            size++;

            for (int i = 0; i < 4; i++)
            {
                int adj_i = curr.first + directions[i].first;
                int adj_j = curr.second + directions[i].second;

                if (0 > adj_i || adj_i >= M || 0 > adj_j || adj_j >= N)
                {
                    continue;
                }
                if (grid[adj_i][adj_j] == 0)
                {
                    continue;
                }
                q.push({adj_i, adj_j});
                grid[adj_i][adj_j] = 0;
            }
        }

        return size;
    }
    int maxAreaOfIsland(vector<vector<int>> &grid)
    {
        int M = grid.size();
        int N = grid[0].size();
        int max_area = 0;
        for (int i = 0; i < M; i++)
        {
            for (int j = 0; j < N; j++)
            {
                if (grid[i][j] == 1)
                {
                    max_area = max(max_area, getArea(i, j, M, N, grid));
                }
            }
        }
        return max_area;
    }
};

int main()
{
    Solution solution;
    vector<vector<int>> grid = {
        {0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0},
        {0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0},
        {0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0},
        {0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0},
        {0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0}};
    cout << solution.maxAreaOfIsland(grid) << endl;
    return 0;
}