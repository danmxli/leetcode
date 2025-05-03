#include <iostream>
#include <print>
#include <vector>
#include <queue>
#include <climits>
using namespace std;

// edge traversal has a weight of `time`
// traffic light alternates from green <-> red every `change`

class Solution
{
public:
    int secondMinimum(int n, vector<vector<int>> &edges, int time, int change)
    {
        // unweighted, undirected graph - nodes are 1-indexed
        vector<vector<int>> graph(n);
        vector<int> weights_1(n, INT_MAX);
        vector<int> weights_2(n, INT_MAX);

        // first is cost, second is node-1
        queue<pair<int, int>> q;

        // init from node "1"
        for (int i = 0; i < edges.size(); i++)
        {
            int source = edges[i][0] - 1;
            int destination = edges[i][1] - 1;
            graph[source].push_back(destination);
            graph[destination].push_back(source);
        }
        weights_1[0] = 0;
        q.push({0, 0});

        while (!q.empty())
        {
            auto [curr_weight, curr_node] = q.front();
            q.pop();
            for (auto adj_node : graph[curr_node])
            {
                int new_weight = curr_weight + time;
                // additional waiting time at red signal
                if ((curr_weight / change) % 2 == 1)
                {
                    new_weight += change - (curr_weight % change);
                }

                // edge relaxation
                if (weights_1[adj_node] > new_weight)
                {
                    // update first and second minimum times
                    weights_2[adj_node] = weights_1[adj_node];
                    weights_1[adj_node] = new_weight;
                    q.push({new_weight, adj_node});
                }
                else if (weights_1[adj_node] < new_weight && weights_2[adj_node] > new_weight)
                {
                    // maintain the second minimum time
                    weights_2[adj_node] = new_weight;
                    q.push({new_weight, adj_node});
                }
            }
        }

        return weights_2[n - 1];
    }
};

int main()
{
    Solution solution;
    int n = 5;
    vector<vector<int>> edges = {{1, 2}, {1, 3}, {1, 4}, {3, 4}, {4, 5}};
    int time = 3;
    int change = 5;
    cout << solution.secondMinimum(n, edges, time, change) << endl;
    return 0;
}