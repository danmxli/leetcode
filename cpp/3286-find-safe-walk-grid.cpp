#include <iostream>
#include <print>
#include <deque>
#include <vector>
#include <climits>
using namespace std;

// intuition: 01 bfs
// similar to dijkstra's algorithm, but uses a deque instead of min pq
// shortest path edge relaxation

class Solution
{
public:
    bool findSafeWalk(vector<vector<int>> &grid, int health)
    {
        int M = grid.size();
        int N = grid[0].size();
        deque<pair<pair<int, int>, int>> dq;
        vector<vector<int>> weights(M, vector<int>(N, INT_MAX));
        vector<pair<int, int>> directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        // init
        int start_weight = grid[0][0];
        dq.push_back({{0, 0}, start_weight});
        weights[0][0] = start_weight;

        while (!dq.empty())
        {
            auto curr = dq.front();
            int curr_m = curr.first.first;
            int curr_n = curr.first.second;
            int curr_w = curr.second;

            // return if reached destination
            if (curr_m == M - 1 && curr_n == N - 1)
            {
                return true;
            }
            dq.pop_front();

            for (int i = 0; i < 4; i++)
            {
                int adj_m = curr_m + directions[i].first;
                int adj_n = curr_n + directions[i].second;

                if (0 > adj_m || adj_m >= M || 0 > adj_n || adj_n >= N)
                {
                    continue;
                }
                int adj_w = grid[adj_m][adj_n];
                int new_w = adj_w + curr_w;
                if (new_w >= health)
                {
                    continue;
                }

                // edge relaxation
                if (weights[adj_m][adj_n] > new_w)
                {
                    weights[adj_m][adj_n] = new_w;
                    if (adj_w == 1)
                    {
                        dq.push_back({{adj_m, adj_n}, new_w});
                    }
                    else
                    {
                        dq.push_front({{adj_m, adj_n}, new_w});
                    }
                }
            }
        }

        // exhausted exploration
        return false;
    }
};

int main()
{
    Solution solution;
    // vector<vector<int>> grid = {{0, 1, 1, 0, 0, 0}, {1, 0, 1, 0, 0, 0}, {0, 1, 1, 1, 0, 1}};
    vector<vector<int>> grid = {{1, 1, 1, 1}};
    int health = 4;
    cout << (solution.findSafeWalk(grid, health) ? "TRUE" : "FALSE") << endl;
}