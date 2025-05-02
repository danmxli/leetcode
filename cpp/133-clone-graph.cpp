#include <vector>
#include <unordered_map>
#include <queue>
using namespace std;

// Definition for a Node.
class Node
{
public:
    int val;
    vector<Node *> neighbors;
    Node()
    {
        val = 0;
        neighbors = vector<Node *>();
    }
    Node(int _val)
    {
        val = _val;
        neighbors = vector<Node *>();
    }
    Node(int _val, vector<Node *> _neighbors)
    {
        val = _val;
        neighbors = _neighbors;
    }
};

class Solution
{
public:
    Node *bfsHelper(Node *node)
    {
        // maintain a hashmap of node objects where key is original, value is cloned
        // bfs approach
        unordered_map<Node *, Node *> visited;
        queue<Node *> q;

        // init
        Node *clone = new Node(node->val);
        visited[node] = clone;
        q.push(node);

        while (!q.empty())
        {
            Node *curr_node = q.front();
            q.pop();

            for (Node *adj_node : curr_node->neighbors)
            {
                // if adjacent node not visited, clone and store it in the hashmap
                if (visited.find(adj_node) == visited.end())
                {
                    visited[adj_node] = new Node(adj_node->val);
                    q.push(adj_node);
                }
                // push it to the neighbors of the current node
                visited[curr_node]->neighbors.push_back(visited[adj_node]);
            }
        }
        return clone;
    }

    Node *dfsHelper(Node *node, unordered_map<Node *, Node *> &visited)
    {
        if (visited.find(node) != visited.end())
        {
            return visited[node];
        }
        Node *clone = new Node(node->val);
        visited[node] = clone;

        for (Node *adj_node : node->neighbors)
        {
            Node *adj_clone = dfsHelper(adj_node, visited);
            visited[node]->neighbors.push_back(adj_clone);
        }
        return clone;
    }
    Node *cloneGraph(Node *node)
    {
        if (!node)
        {
            return nullptr;
        }
        unordered_map<Node *, Node *> visited;
        return bfsHelper(node);
    }
};