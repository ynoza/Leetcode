# https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        lst=[]
        done=False
        def recur(root, voyage):
            nonlocal lst, done
            if root==None or done: return
            elif root.left and root.right:
                if voyage[0]==root.left.val: 
                    voyage.pop(0)
                elif voyage[0]==root.right.val: 
                    temp=root.left
                    root.left=root.right
                    root.right=temp
                    lst.append(root.val)
                    voyage.pop(0)
                else:
                    lst.append(-1)
                    done=True
                    return
            elif root.left:
                if root.left.val!=voyage[0]: 
                    lst.append(-1)
                    done=True
                    return
                voyage.pop(0)
                
            recur(root.left,voyage)
            
            if root.right:
                if root.right.val!=voyage[0]: 
                    lst.append(-1)
                    done=True
                    return
                voyage.pop(0)
                
            recur(root.right,voyage)
        
        # print(root.val)
        if root==None: 
            return []
        elif root.val!=voyage[0]: 
            return [-1]
        
        voyage.pop(0)
        recur(root,voyage)
        # print(voyage)
        if done: return [-1] 
        return lst