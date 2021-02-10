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
    TreeNode* convertBST(TreeNode* root) {
    TreeNode *curr=root;
     int ret=0;
     vector<TreeNode*> stack;
     while(curr!=NULL || stack.size()>0){
        while (curr!=NULL){
            // cout << curr->val << endl;
            stack.emplace_back(curr);
            curr=curr->right;
        }
        curr=stack[stack.size()-1];
        // if (curr) cout << stack[stack.size()-1]->val << " " << ret<< endl;
        stack.pop_back();
        curr->val+=ret;
        ret=curr->val;
        curr=curr->left;
        
        
    }
        return root;
    }
};