#include <iostream>
#include <print>
#include <vector>
#include <queue>
#include <set>
using namespace std;

class Solution
{
public:
    void bfsHelper(vector<vector<int>> &heights, queue<pair<int, int>> &q, vector<vector<bool>> &seen, int M, int N)
    {
        vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        while (!q.empty())
        {
            auto curr = q.front();
            int i = curr.first;
            int j = curr.second;
            q.pop();

            for (int k = 0; k < 4; k++)
            {
                int adj_i = i + directions[k].first;
                int adj_j = j + directions[k].second;

                if (0 > adj_i || adj_i >= M || 0 > adj_j || adj_j >= N || seen[adj_i][adj_j])
                {
                    continue;
                }
                if (heights[i][j] <= heights[adj_i][adj_j])
                {
                    seen[adj_i][adj_j] = true;
                    q.push({adj_i, adj_j});
                }
            }
        }
    }
    vector<vector<int>> pacificAtlantic(vector<vector<int>> &heights)
    {
        int M = heights.size();
        int N = heights[0].size();
        queue<pair<int, int>> p_q;
        queue<pair<int, int>> a_q;
        vector<vector<bool>> p_seen(M, vector<bool>(N, false));
        vector<vector<bool>> a_seen(M, vector<bool>(N, false));

        for (int i = 0; i < M; i++)
        {
            p_q.push({i, 0});
            p_seen[i][0] = true;
            a_q.push({i, N - 1});
            a_seen[i][N - 1] = true;
        }
        for (int j = 0; j < N; j++)
        {
            p_q.push({0, j});
            p_seen[0][j] = true;
            a_q.push({M - 1, j});
            a_seen[M - 1][j] = true;
        }

        bfsHelper(heights, p_q, p_seen, M, N);
        bfsHelper(heights, a_q, a_seen, M, N);

        vector<vector<int>> soln = {};
        for (int i = 0; i < M; i++)
        {
            for (int j = 0; j < N; j++)
            {
                if (p_seen[i][j] && a_seen[i][j])
                {
                    soln.push_back({i, j});
                }
            }
        }
        return soln;
    }
};

int main()
{
    Solution solution;
    vector<vector<int>> heights = {{1, 2, 2, 3, 5},
                                   {3, 2, 3, 4, 4},
                                   {2, 4, 5, 3, 1},
                                   {6, 7, 1, 4, 5},
                                   {5, 1, 1, 2, 4}};
    print("{}\n", solution.pacificAtlantic(heights));
    return 0;
}