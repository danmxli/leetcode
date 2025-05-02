#include <iostream>
#include <print>
#include <vector>
#include <queue>
using namespace std;

class Solution
{
public:
    vector<int> floodFill(int M, int N, vector<vector<int>> &grid, int i, int j)
    {
        // insert the coordinates
        vector<int> group = {i, j, i, j};

        queue<pair<int, int>> q;
        vector<pair<int, int>> directions = {{1, 0}, {0, 1}};
        q.push({i, j});

        while (!q.empty())
        {
            auto curr = q.front();
            q.pop();

            for (int i = 0; i < 2; i++)
            {
                int adj_i = curr.first + directions[i].first;
                int adj_j = curr.second + directions[i].second;

                if (0 > adj_i || adj_i >= M || 0 > adj_j || adj_j >= N || grid[adj_i][adj_j] == 0)
                {
                    continue;
                }
                grid[adj_i][adj_j] = 0;
                group[2] = max(group[2], adj_i);
                group[3] = max(group[3], adj_j);
                q.push({adj_i, adj_j});
            }
        }

        return group;
    }
    vector<vector<int>> findFarmland(vector<vector<int>> &land)
    {
        int M = land.size();
        int N = land[0].size();
        vector<vector<int>> ans = {};

        for (int i = 0; i < M; i++)
        {
            for (int j = 0; j < N; j++)
            {
                if (land[i][j] == 1)
                {
                    ans.push_back(floodFill(M, N, land, i, j));
                }
            }
        }

        return ans;
    }
};

int main()
{
    Solution solution;
    vector<vector<int>> land = {{1, 0, 0}, {0, 1, 1}, {0, 1, 1}};
    print("{}\n", solution.findFarmland(land));
    return 0;
}