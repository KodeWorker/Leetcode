# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        string = ""
        if t != None:
            string += str(t.val)
            if t.left != None and t.right != None:
                string += "(%s)(%s)" %(self.tree2str(t.left), self.tree2str(t.right))
            elif t.left != None:
                string += "(%s)" %(self.tree2str(t.left))
            elif t.right != None:
                string += "()(%s)" %(self.tree2str(t.right))        
        return string

if __name__ == '__main__':
#    t1 = TreeNode(1)
#    t1.left = TreeNode(2)
#    t1.left.left = TreeNode(4)
#    t1.right = TreeNode(3)
    
    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    t1.left.right = TreeNode(4)
    
    t1.right = TreeNode(3)

    sol = Solution()
    string = sol.tree2str(t1)
    print(string)