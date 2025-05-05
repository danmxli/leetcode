#include <iostream>
#include <print>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution
{
public:
    vector<double> averageOfLevels(TreeNode *root)
    {
        vector<double> ans;
        queue<TreeNode *> q;

        // init
        q.push(root);
        ans.push_back(root->val);

        while (!q.empty())
        {
            // 😭
            long long levelValues = 0;
            int l = q.size();
            int nodeCount = 0;
            for (int i = 0; i < l; i++)
            {
                TreeNode *curr = q.front();
                q.pop();

                if (curr->left)
                {
                    q.push(curr->left);
                    levelValues += curr->left->val;
                    nodeCount++;
                }
                if (curr->right)
                {
                    q.push(curr->right);
                    levelValues += curr->right->val;
                    nodeCount++;
                }
            }
            if (nodeCount > 0)
            {
                // 😭
                ans.push_back(levelValues / (double)nodeCount);
            }
        }

        return ans;
    }
};

int main()
{
    TreeNode *root = new TreeNode(3);
    root->left = new TreeNode(9);
    root->right = new TreeNode(20);
    root->right->left = new TreeNode(15);
    root->right->right = new TreeNode(7);

    Solution solution;
    print("{}\n", solution.averageOfLevels(root));

    return 0;
}