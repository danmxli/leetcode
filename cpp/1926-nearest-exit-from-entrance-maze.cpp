#include <iostream>
#include <print>
#include <vector>
#include <queue>
using namespace std;

class Solution
{
public:
    int nearestExit(vector<vector<char>> &maze, vector<int> &entrance)
    {
        int M = maze.size();
        int N = maze[0].size();
        queue<pair<int, int>> q;
        vector<vector<bool>> seen(M, vector<bool>(N, false));
        vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        int level = -1;

        q.push({entrance[0], entrance[1]});
        seen[entrance[0]][entrance[1]] = true;

        while (!q.empty())
        {
            level++;
            int l = q.size();
            for (int i = 0; i < l; i++)
            {
                auto curr = q.front();
                q.pop();

                for (int i = 0; i < 4; i++)
                {
                    int adj_i = curr.first + directions[i].first;
                    int adj_j = curr.second + directions[i].second;

                    if (0 > adj_i || adj_i >= M || 0 > adj_j || adj_j >= N)
                    {
                        if (curr.first == entrance[0] && curr.second == entrance[1])
                        {
                            continue;
                        }
                        return level;
                    }
                    if (seen[adj_i][adj_j] || maze[adj_i][adj_j] == '+')
                    {
                        continue;
                    }
                    q.push({adj_i, adj_j});
                    seen[adj_i][adj_j] = true;
                }
            }
        }

        return -1;
    }
};

int main()
{
    Solution solution;
    // vector<vector<char>> maze = {{'+', '+', '.', '+'}, {'.', '.', '.', '+'}, {'+', '+', '+', '.'}};
    vector<vector<char>> maze = {{'+', '+', '+'}, {'.', '.', '.'}, {'+', '+', '+'}};
    vector<int> entrance = {1, 0};
    cout << solution.nearestExit(maze, entrance) << endl;
    return 0;
}