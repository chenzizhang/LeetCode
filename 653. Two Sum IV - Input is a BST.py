# #Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:       
    def findHelper(self, root, k, visited):
        if root is None:
            return False
        
        other = k - root.val
        if other in visited:
            return True
        else:
            visited.extend([root.val])
        
        return self.findHelper(root.left, k, visited) or self.findHelper(root.right, k, visited)
    
    
    def findTarget(self, root: TreeNode, k: int) -> bool:
        visited = list()
        return self.findHelper(root, k, visited)