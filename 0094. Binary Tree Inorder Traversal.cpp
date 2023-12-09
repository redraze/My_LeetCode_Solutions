/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        std::vector<TreeNode*> stack;
        std::vector<int> ret;

        DFS(stack, root);

        while (!stack.empty()) {
            TreeNode* node = stack.back();
            stack.pop_back();
            ret.push_back(node->val);
            DFS(stack, node->right);
        }

        return ret; 
    }
private:
    void DFS(vector<TreeNode*> &stack, TreeNode* &node) {
        while(node) {
            stack.push_back(node);
            node = node->left;
        }
    }
};
