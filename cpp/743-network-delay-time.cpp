#include <iostream>
#include <print>
#include <vector>
#include <queue>
#include <functional>
#include <algorithm>
#include <climits>
using namespace std;

class Solution
{
public:
    int networkDelayTime(vector<vector<int>> &times, int n, int k)
    {
        // weighted, directed graph - nodes are 1-indexed
        vector<vector<pair<int, int>>> graph(n);
        // min priority queue - first is weight, second is node
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> min_pq;
        // weights
        vector<int> weights(n, INT_MAX);

        // init from node k
        for (int i = 0; i < times.size(); i++)
        {
            int source = times[i][0] - 1;
            int destination = times[i][1] - 1;
            int weight = times[i][2];
            graph[source].push_back({weight, destination});
        }
        weights[k - 1] = 0;
        min_pq.push({0, k - 1});

        while (!min_pq.empty())
        {
            auto curr = min_pq.top();
            int c_weight = curr.first;
            int c_node = curr.second;
            min_pq.pop();

            for (int i = 0; i < graph[c_node].size(); i++)
            {
                int adj_weight = graph[c_node][i].first;
                int adj_node = graph[c_node][i].second;

                // edge relaxation
                int new_weight = c_weight + adj_weight;

                if (weights[adj_node] > new_weight)
                {
                    weights[adj_node] = new_weight;
                    min_pq.push({new_weight, adj_node});
                }
            }
        }

        // get the max element from the weights, since that will be the time for the furthest node to receive the signal
        // note: cpp algorithms library
        int time = *max_element(weights.begin(), weights.end());
        if (time == INT_MAX)
        {
            return -1;
        }
        return time;
    }
};

int main()
{
    Solution solution;
    vector<vector<int>> times = {{2, 1, 1}, {2, 3, 1}, {3, 4, 1}};
    int n = 4;
    int k = 2;
    cout << solution.networkDelayTime(times, n, k) << endl;
    return 0;
}