# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        sum = self.getSum(l1) + self.getSum(l2)
        l3 = self.genListNode(sum)
        return l3
        
    def getSum(self, listNode):
        if listNode.next != None:
            return listNode.val + 10 * self.getSum(listNode.next)
        else:
            return listNode.val
    
    def genListNode(self, sum):
        numString = str(sum)
        val = int(numString[-1])
        if len(numString[:-1]) > 0:
            next = self.genListNode(int(numString[:-1]))
        else:
            next = None
        LN = ListNode(val)
        LN.next = next
        return LN

def recPrint(listNode):
    if listNode.next != None:
        print(listNode.val)
        recPrint(listNode.next)
    else:
        print(listNode.val)

if __name__ == '__main__':
    # l1: [2,4,5]
    # l2: [5,6,4]
    # l3: [7,0,8]
    
    #l1
        n3 = ListNode(5)
        n2 = ListNode(4)
        n2.next = n3
        l1 = ListNode(2)
        l1.next = n2
        
        n5 = ListNode(4)
        n4 = ListNode(6)
        n4.next = n5
        l2 = ListNode(5)
        l2.next = n4
        
        sol = Solution()
        print(sol.getSum(l2))
        l3 = sol.addTwoNumbers(l1,l2)
        recPrint(l3)


        