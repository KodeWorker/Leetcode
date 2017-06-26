class MyStack(object):
    
    def __init__(self):
        self.top = -1
        self.stack = []
        
    def push(self, x):
        self.top += 1
        self.stack.append(x)
    
    def pop(self):
        if not self.empty():
            self.top -= 1
            return self.stack.pop() 
        else:
            return None
    
    def empty(self):
        if len(self.stack) <= 0:
            return True
        else:
            return False

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_front = MyStack()
        self.stack_rare = MyStack()

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack_rare.push(x)
        
    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        while not self.stack_rare.empty():
            self.stack_front.push(self.stack_rare.pop())
            
        output = self.stack_front.pop()
        
        while not self.stack_front.empty():
            self.stack_rare.push(self.stack_front.pop())
            
        return output   

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        while not self.stack_rare.empty():
            self.stack_front.push(self.stack_rare.pop())
        
        if not self.stack_front.empty():
            output = self.stack_front.stack[self.stack_front.top]
        else:
            output = None
        
        while not self.stack_front.empty():
            self.stack_rare.push(self.stack_front.pop())
    
        return output
    
    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if self.stack_rare.empty():
            return True
        else:
            return False
        
        
if __name__ == '__main__':
    # Your MyQueue object will be instantiated and called as such:
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    x = obj.peek()
    
    print(x)