#include <iostream>
#include <print>
#include <vector>
#include <queue>
#include <functional>
#include <climits>
#include <float.h>

using namespace std;

class Solution
{
public:
    double maxProbability(int n, vector<vector<int>> &edges,
                          vector<double> &succProb, int start_node,
                          int end_node)
    {
        // undirected, weighted graph
        vector<vector<pair<double, int>>> graph(n);
        for (int i = 0; i < edges.size(); i++)
        {
            int source = edges[i][0];
            int dest = edges[i][1];
            double weight = succProb[i];

            graph[source].push_back({weight, dest});
            graph[dest].push_back({weight, source});
        }

        // using max pq, due to "monotonic nature" of probability
        priority_queue<pair<double, int>> pq;
        vector<double> weights(n, 0);

        weights[start_node] = 1;
        pq.push({1, start_node});

        while (!pq.empty())
        {
            auto [curr_weight, curr_node] = pq.top();
            pq.pop();

            for (auto [adj_weight, adj_node] : graph[curr_node])
            {
                // edge relaxation
                double new_weight = curr_weight * adj_weight;
                if (weights[adj_node] < new_weight)
                {
                    weights[adj_node] = new_weight;
                    pq.push({new_weight, adj_node});
                }
            }
        }

        return weights[end_node];
    }
};

int main()
{
    Solution solution;
    int n = 3;
    vector<vector<int>> edges = {{0, 1}, {1, 2}, {0, 2}};
    vector<double> succProb = {0.5, 0.5, 0.2};
    int start_node = 0;
    int end_node = 2;

    cout << solution.maxProbability(n, edges, succProb, start_node, end_node) << endl;
    return 0;
}