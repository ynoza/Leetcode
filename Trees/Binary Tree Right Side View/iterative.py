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
    // void helper(TreeNode* root, vector<int> & v, int level){
    //     if (root==NULL) return;
    //     else if (level>=v.size()) v.emplace_back(root->val);
    //     helper(root->right,v,level+1);
    //     helper(root->left,v,level+1);
    //     return;
    // }
    vector<int> rightSideView(TreeNode* root) {
        int level=0;
        vector<int> v;
        vector<int> s;
        vector<TreeNode *> stack;
        while (root || stack.size()>0){
            while(root){
                if (level>=v.size()) v.emplace_back(root->val);
                stack.emplace_back(root);
                s.emplace_back(level);
                root=root->right;
                level++;
            }    
            root = stack[stack.size()-1];
            level = s[s.size()-1];
            s.pop_back();
            stack.pop_back();
            if (root->left) {
                root=root->left;
                level+=1;
            }
            else root=NULL;
            
        }
        return v;
    }
};