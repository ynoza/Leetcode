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
    void helper(TreeNode * root, vector<vector<int>> & v, int level){
        if (root==NULL) return;
        else if (level>=v.size()) {
            vector<int> l;
            l.emplace_back(root->val);
            v.emplace_back(l);
        }
        else if (level%2!=0)  {
            v[level].insert(v[level].begin(),root->val);
        }
        else v[level].emplace_back(root->val);
        helper(root->left,v,level+1);
        helper(root->right,v,level+1);
        return;
    }
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> v;
        helper(root,v,0);
        return v;
    }
};