#include <iostream>
#include <print>
#include <vector>
#include <queue>
#include <functional>
#include <climits>

// cpp optimization
// grid data at (i,j) stored in flat array as [i * N + j]
// flat array has a size of M * N
// map 1D index to 2D grid coords:
// i = index / N
// j = index mod N

// candidate edge is determined by the max of current node weight and grid value of adjacent node

using namespace std;

class Solution
{
public:
    int swimInWater(vector<vector<int>> &grid)
    {
        int N = grid.size();
        vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        // weight, nodeid
        // priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, greater<pair<int, pair<int, int>>>> pq;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        vector<int> weights(N * N, INT_MAX);

        // init from (0, 0)
        pq.push({0, 0});
        weights[0] = grid[0][0];

        while (!pq.empty())
        {
            auto [curr_weight, curr_node] = pq.top();
            if ((curr_node / N) == N - 1 && (curr_node % N) == N - 1)
            {
                return curr_weight;
            }
            pq.pop();

            for (auto [i, j] : directions)
            {
                int adj_i = (curr_node / N) + i;
                int adj_j = (curr_node % N) + j;
                int adj_node = adj_i * N + adj_j;

                if (0 > adj_i || adj_i >= N || 0 > adj_j || adj_j >= N)
                {
                    continue;
                }

                int candidate_weight = max(weights[curr_node], grid[adj_i][adj_j]);
                if (weights[adj_node] > candidate_weight)
                {
                    weights[adj_node] = candidate_weight;
                    pq.push({candidate_weight, adj_node});
                }
            }
        }

        return -1;
    }
};

int main()
{
    Solution solution;
    vector<vector<int>> grid = {{3, 2}, {0, 1}};
    cout << solution.swimInWater(grid) << endl;
    return 0;
}