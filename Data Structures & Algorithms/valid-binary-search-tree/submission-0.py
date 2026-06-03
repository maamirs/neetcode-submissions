# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return
        

        def dfs(node, minval, maxval):
            if not node:
                return True
            
            if node.val <= minval or node.val >= maxval:
                return False
            

            leftvalid = dfs(node.left, minval, node.val)
            rightvalid = dfs(node.right, node.val, maxval)


            return leftvalid and rightvalid
        

        return dfs(root, float('-inf'), float('inf'))
        