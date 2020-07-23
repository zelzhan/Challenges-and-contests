# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        visited = [0]
        
        res = []
        
        def traverse(node):
            if res or not node:
                return

            left = traverse(node.left)
            if left:
                return left
            
            visited[0]+=1
            
            if visited[0] == k:
                res.append(node.val)
            
            right = traverse(node.right)

        
        traverse(root)
        
        return res[0]
