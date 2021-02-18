# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
result=[]
def inorder(root):
    if not root:
        return root
    inorder(root.left)
    result.append(root.val)    
    inorder(root.right)
    
    
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        global result
        result=[]
        inorder(root)
        return result
    
        
        
        
        
        
        