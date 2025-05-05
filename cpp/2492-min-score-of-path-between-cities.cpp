#include <iostream>
#include <print>
#include <queue>
#include <vector>
#include <climits>
using namespace std;

// return the minimum edge weight that can be reached from node 1

class Solution
{
public:
    int minScore(int n, vector<vector<int>> &roads)
    {
        // undirected weighted graph (weight, destination) - nodes are 1-indexed
        vector<vector<pair<int, int>>> graph(n);
        for (int i = 0; i < roads.size(); i++)
        {
            int source = roads[i][0] - 1;
            int dest = roads[i][1] - 1;
            int weight = roads[i][2];
            graph[source].push_back({weight, dest});
            graph[dest].push_back({weight, source});
        }
        queue<int> q;
        vector<bool> visited(n, false);

        // init from node "1"
        q.push(0);
        visited[0] = true;
        int min_weight = INT_MAX;

        while (!q.empty())
        {
            int curr_node = q.front();
            q.pop();

            for (auto [adj_weight, adj_node] : graph[curr_node])
            {
                // DO VALUE COMPARISON BEFORE ADDING TO QUEUE
                min_weight = min(min_weight, adj_weight);
                if (visited[adj_node])
                {
                    continue;
                }
                q.push(adj_node);
                visited[adj_node] = true;
            }
        }

        return min_weight;
    }
};

int main()
{
    int n = 4;
    vector<vector<int>> roads = {{1, 2, 9}, {2, 3, 6}, {2, 4, 5}, {1, 4, 7}};

    Solution solution;
    cout << solution.minScore(n, roads) << endl;

    return 0;
}