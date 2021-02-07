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
    void helper(TreeNode* root, vector<int> & v, int level){
        if (root==NULL) return;
        else if (level>=v.size()) v.emplace_back(root->val);
        helper(root->right,v,level+1);
        helper(root->left,v,level+1);
        return;
    }
    vector<int> rightSideView(TreeNode* root) {
        vector<int> v;
        helper(root,v, 0);
        return v;
    }
};
