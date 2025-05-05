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
    vector<vector<int>> levelOrderBottom(TreeNode *root)
    {
        vector<vector<int>> ans;
        queue<TreeNode *> q;

        if (!root)
        {
            return ans;
        }
        // init
        q.push(root);
        ans.push_back({root->val});

        while (!q.empty())
        {
            vector<int> levelValues = {};
            int l = q.size();
            for (int i = 0; i < l; i++)
            {
                TreeNode *curr = q.front();
                q.pop();
                if (curr->left)
                {
                    levelValues.push_back(curr->left->val);
                    q.push(curr->left);
                }
                if (curr->right)
                {
                    levelValues.push_back(curr->right->val);
                    q.push(curr->right);
                }
            }
            if (!levelValues.empty())
            {
                ans.push_back(levelValues);
            }
        }

        reverse(ans.begin(), ans.end());
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
    print("{}\n", solution.levelOrderBottom(root));
    return 0;
}