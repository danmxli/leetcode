#include <vector>
#include <iostream>
#include <queue>
#include <set>
#include <print>
using namespace std;

class Solution
{
public:
    bool canFinish(int numCourses, vector<vector<int>> &prerequisites)
    {
        // maintain a set of remaining nodes
        set<int> nodes;
        for (int i = 0; i < numCourses; i++)
        {
            nodes.insert(i);
        }

        // build the adjacency list
        vector<vector<int>> graph(numCourses);
        for (int i = 0; i < prerequisites.size(); i++)
        {
            graph[prerequisites[i][1]].push_back(prerequisites[i][0]);
        }

        // build the indegree array
        vector<int> indegree(numCourses, 0);
        for (int i = 0; i < prerequisites.size(); i++)
        {
            indegree[prerequisites[i][0]]++;
        }

        // push all the nodes with indegree 0 into the queue
        queue<int> q;
        for (int i = 0; i < numCourses; i++)
        {
            if (indegree[i] == 0)
            {
                q.push(i);
                nodes.erase(i);
            }
        }

        while (!q.empty())
        {
            int curr = q.front();
            q.pop();
            for (int i = 0; i < graph[curr].size(); i++)
            {
                int adj = graph[curr][i];
                indegree[adj]--;
                if (indegree[adj] == 0)
                {
                    q.push(adj);
                    nodes.erase(adj);
                }
            }
        }

        if (!nodes.empty())
        {
            return false;
        }
        return true;
    }
};

int main()
{
    Solution solution;
    int numCourses = 2;
    vector<vector<int>> prerequisites = {{1, 0}, {0, 1}};
    // vector<vector<int>> prerequisites = {{1, 0}};
    cout << (solution.canFinish(numCourses, prerequisites) ? "YES" : "NO") << endl;
    return 0;
}
