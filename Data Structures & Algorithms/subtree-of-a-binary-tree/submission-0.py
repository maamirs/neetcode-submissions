# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # first find the subroot
        # then start comparing dfs way


        
        def isSameTree(node1, node2):
             
            if not node1 and not node2:
               return True
            
            if not node1 or not node2:
                return False
            
            if node1.val != node2.val:
                return False
            
            leftvalid = isSameTree(node1.left, node2.left)
            rightvalid = isSameTree(node1.right, node2.right)

            return leftvalid and rightvalid



        def dfs(node):
            if not node:
                return False
            
            if node.val == subRoot.val and isSameTree(node, subRoot):
                return True
            
            leftcontains = dfs(node.left)
            rightcontains = dfs(node.right)

            return(leftcontains or rightcontains)


        return dfs(root)


        