
    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        ans=root
        def helper(parent, root):
            if root==None:
                return
            elif root.val < low:
                if root.right!=None:
                    root.val=root.right.val
                    root.left=root.right.left
                    root.right=root.right.right
                    helper(parent, root)
                    return
                else:
                    parent.left=None
                    # print(root)
                    return
            elif root.val > high:
                if root.left!=None:
                    root.val=root.left.val
                    root.right=root.left.right
                    root.left=root.left.left
                    helper(parent, root)
                    return
                else:
                    parent.right=None
                    return
            # if (root.val==low): root.left=None
            # if (root.val==high): root.right=None
                
            helper(root, root.left)
            helper(root, root.right)
        helper(None,root)
        return root