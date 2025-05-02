#include <vector>
#include <queue>
using namespace std;

class Solution
{
public:
    int floodFill(int M, int N, vector<vector<int>> &grid, vector<vector<int>> &reference, int i, int j)
    {
        int isValid = 1;
        if (reference[i][j] != 1)
        {
            isValid = 0;
        }
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

                if (0 > adj_i || adj_i >= M || 0 > adj_j || adj_j >= N || grid[adj_i][adj_j] == 0)
                {
                    continue;
                }
                if (reference[adj_i][adj_j] != 1)
                {
                    isValid = 0;
                }
                grid[adj_i][adj_j] = 0;
                q.push({adj_i, adj_j});
            }
        }
        return isValid;
    }
    int countSubIslands(vector<vector<int>> &grid1, vector<vector<int>> &grid2)
    {
        int M = grid1.size();
        int N = grid1[0].size();
        int count = 0;

        for (int i = 0; i < M; i++)
        {
            for (int j = 0; j < N; j++)
            {
                if (grid2[i][j] == 1)
                {
                    count += floodFill(M, N, grid2, grid1, i, j);
                }
            }
        }
        return count;
    }
};