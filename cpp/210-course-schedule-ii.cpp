#include <iostream>
#include <print>
#include <vector>
#include <queue>
#include <set>
using namespace std;

class Solution
{
public:
    vector<int> findOrder(int numCourses, vector<vector<int>> &prerequisites)
    {
        // build the set of initial remaining courses
        set<int> rem_courses;
        for (int i = 0; i < numCourses; i++)
        {
            rem_courses.insert(i);
        }

        // construct the graph
        vector<vector<int>> graph(numCourses);
        for (int i = 0; i < prerequisites.size(); i++)
        {
            // int source = prerequisites[i][1];
            // int dest = prerequisites[i][0];
            graph[prerequisites[i][1]].push_back(prerequisites[i][0]);
        }

        // get the in-degree of each course
        vector<int> indegree(numCourses, 0);
        for (int i = 0; i < prerequisites.size(); i++)
        {
            indegree[prerequisites[i][0]]++;
        }

        // build the queue
        queue<int> q;
        vector<int> course_order = {};
        for (int i = 0; i < numCourses; i++)
        {
            if (indegree[i] == 0)
            {
                q.push(i);
                rem_courses.erase(i);
            }
        }

        while (!q.empty())
        {
            int curr = q.front();
            course_order.push_back(curr);
            q.pop();

            // adjacent exploration
            for (int i = 0; i < graph[curr].size(); i++)
            {
                int adj = graph[curr][i];
                indegree[adj]--;
                if (indegree[adj] == 0)
                {
                    q.push(adj);
                    rem_courses.erase(adj);
                }
            }
        }

        if (!rem_courses.empty())
        {
            return {};
        }
        return course_order;
    }
};

int main()
{
    Solution solution;
    int numCourses = 4;
    vector<vector<int>> prerequisites = {{1, 0}, {2, 0}, {3, 1}};

    print("{}\n", solution.findOrder(numCourses, prerequisites));

    return 0;
}