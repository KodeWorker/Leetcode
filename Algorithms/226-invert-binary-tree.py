# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root != None:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)         
        return root
    
if __name__ == '__main__':

    
    t1 = TreeNode(4)
    t1.left = TreeNode(2)
    t1.left.left = TreeNode(1)
    t1.left.right = TreeNode(3)
    
    t1.right = TreeNode(7)
    t1.right.left = TreeNode(6)
    t1.right.right = TreeNode(9)

    sol = Solution()
    sol.invertTree(t1)


