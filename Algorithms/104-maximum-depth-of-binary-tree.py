# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.checkChild(root)
    
    def checkChild(self, node):
        
        if node == None:
            return 0
        else:
            return 1 + max(self.checkChild(node.left), self.checkChild(node.right))
        

if __name__ == '__main__':
    t = TreeNode(1)
    t.right = TreeNode(2)
    t.right.right = TreeNode(1)
    sol = Solution()
    n = sol.maxDepth(t)
    print(n)