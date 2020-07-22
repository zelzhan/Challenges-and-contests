# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict, deque

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        table = defaultdict(list)
        
        
        def traverse(node, level):
            if node:
                if level%2==0:
                    table[level].append(node.val)
                else:
                    table[level].insert(0, node.val)

                traverse(node.left, level+1)
                traverse(node.right, level+1)
                
        
        traverse(root, 0)
        
        return [table[key] for key in sorted(table.keys())]
