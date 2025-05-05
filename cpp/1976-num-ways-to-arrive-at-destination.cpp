#include <iostream>
#include <print>
#include <vector>
#include <queue>
#include <climits>

using namespace std;

class Solution {
    public:
        int countPaths(int n, vector<vector<int>>& roads) {
            // weighted, undirected graph - first is weight, second is node
            vector<vector<pair<long long, int>>> graph(n);
            for (auto& road : roads) {
                int source = road[0];
                int dest = road[1];
                int weight = road[2];
                graph[source].push_back({weight, dest});
                graph[dest].push_back({weight, source});
            }
            
            // 😭
            const int MOD = 1e9 + 7;
            vector<long long> dist(n, LLONG_MAX);
            vector<long long> ways(n, 0);
            
            // min priority queue - first is weight, second is node
            priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
            
            // init for node 0
            dist[0] = 0;
            ways[0] = 1;
            pq.push({0, 0});
            
            while (!pq.empty()) {
                auto [curr_dist, curr_node] = pq.top();
                pq.pop();
                
                // optimization
                if (curr_dist > dist[curr_node]) continue;
                
                for (auto [edge_weight, adj_node] : graph[curr_node]) {
                    long long new_dist = curr_dist + edge_weight;
                    
                    // edge relaxation - found shortest path
                    if (new_dist < dist[adj_node]) {
                        dist[adj_node] = new_dist;
                        ways[adj_node] = ways[curr_node];
                        pq.push({new_dist, adj_node});
                    }
                    // found another shortest path
                    else if (new_dist == dist[adj_node]) {
                        ways[adj_node] = (ways[adj_node] + ways[curr_node]) % MOD;
                    }
                }
            }
            
            return ways[n-1] % MOD;
        }
    };