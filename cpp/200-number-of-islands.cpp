#include <print>
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Solution
{
public:
    int floodFill(int M, int N, vector<vector<char>> &grid, int i, int j)
    {
        queue<pair<int, int>> q;
        vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        q.push({i, j});

        while (!q.empty())
        {
            auto curr = q.front();
            q.pop();

            for (int i = 0; i < 4; i++)
            {
                int adj_i = curr.first + directions[i].first;
                int adj_j = curr.second + directions[i].second;

                if (0 > adj_i || adj_i >= M || 0 > adj_j || adj_j >= N || grid[adj_i][adj_j] == '0')
                {
                    continue;
                }
                grid[adj_i][adj_j] = '0';
                q.push({adj_i, adj_j});
            }
        }
        return 1;
    }
    int numIslands(vector<vector<char>> &grid)
    {
        int M = grid.size();
        int N = grid[0].size();
        // vector<vector<bool>> visited(M, vector<bool>(N, false));
        int count = 0;

        for (int i = 0; i < M; i++)
        {
            for (int j = 0; j < N; j++)
            {
                if (grid[i][j] == '1')
                {
                    count += floodFill(M, N, grid, i, j);
                }
            }
        }

        return count;
    }
};

int main()
{
    return 0;
}