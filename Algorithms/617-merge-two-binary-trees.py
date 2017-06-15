# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        return self.checkNode(t1, t2)
        
    def checkNode(self, node1, node2):
        
        if node1 == None and node2 == None: # special case
            return None
        elif node1 ==None :
            node3 = TreeNode(node2.val)
        elif node2 == None:
            node3 = TreeNode(node1.val)        
        else:
            node3 = TreeNode(node1.val + node2.val)
        
        if (node1 != None and node1.left != None ) or (node2 != None and node2.left != None):
            if node1 == None:
                node3.left = self.checkNode(None, node2.left)
            elif node2 == None:
                node3.left = self.checkNode(node1.left, None)
            else:
                node3.left = self.checkNode(node1.left, node2.left)
        
        if (node1 != None and node1.right != None) or (node2 != None and node2.right != None):
            if node1 == None:
                node3.right = self.checkNode(None, node2.right)
            elif node2 == None:
                node3.right = self.checkNode(node1.right, None)
            else:
                node3.right = self.checkNode(node1.right, node2.right)
        
        return node3        
               

if __name__ == '__main__':
#    t1 = TreeNode(1)
#    t1.left = TreeNode(3)
#    t1.right = TreeNode(2)
#    t1.left.left = TreeNode(5)
#    
#    t2 = TreeNode(2)
#    t2.left = TreeNode(1)
#    t2.left.right = TreeNode(4)
#    t2.right = TreeNode(3)
#    t2.right.right = TreeNode(7)
    
#    t1=None
#    t2=None

    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    t1.left.right = TreeNode(3)
    
    t2 = TreeNode(1)
    t2.right = TreeNode(2)
    t2.right.right = TreeNode(3)
    
    sol = Solution()
    t3 = sol.mergeTrees(t1, t2)