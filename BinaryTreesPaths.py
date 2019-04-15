# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        paths = []
        def tree_path(node, temp):
            temp.append(str(node.val))
            if node.left:
                tree_path(node.left,temp)
            
            if node.right:
                tree_path(node.right,temp)
            
            if not node.left and not node.right:
                paths.append(temp[:])
            temp.pop()
            
        tree_path(root, [])
        # print(paths)
        return [ "->".join(x) for x in paths]

            
            
            
