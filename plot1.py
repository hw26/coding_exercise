"""
Merge Intervals
"""


"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals):
        # write your code here

        sortedd = []
        for ii in intervals:
            sortedd.append((ii.start,ii.end))
        sortedd.sort()
        l = [Interval(0,-float('inf'))]
        
        last = l[-1]
        for ii in sortedd:
            currentstart = ii[0]
            currentend = ii[1]
            laststart = last.start
            lastend = last.end
            
            if currentstart <= lastend:
                l[-1] = Interval(laststart,max(currentend,lastend))
            else:
                l.append(Interval(currentstart,currentend))
            last = l[-1]
        return l[1:]




"""
Implement Stack by Two Queues 

"""
    


class Stack:
    """
    @param: x: An integer
    @return: nothing
    """
    
    
    
    def __init__(self):
        from collections import deque
        self.q1 = deque([])
        self.q2 = deque([])
    def push(self, x):
        # write your code here
        self.q1.append(x)

    """
    @return: nothing
    """
    def pop(self):
        while len(self.q1) > 1:
            a = self.q1.popleft()
            self.q2.append(a)
        elem = self.q1.popleft()
        
        temp = self.q2
        self.q2 = self.q1
        self.q1 = temp
        return elem
        
        

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        return self.q1[-1]

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        return len(self.q1) == 0



"""
Implement Queue by Two Stacks 

"""

class MyQueue:
    
    def __init__(self):
        # do intialization if necessary
        self.stack1 = []
        self.stack2 = []

    """
    @param: element: An integer
    @return: nothing
    """
    def push(self, element):
        # write your code here
        self.stack1.append(element)
        # print 'stack1', self.stack1
    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        # print self.stack2
        if len(self.stack2) > 0:
            ret = self.stack2.pop()
            return ret
        for i in range(len(self.stack1)):
            a = self.stack1.pop()
            self.stack2.append(a)

        return self.stack2.pop()
        

    """
    @return: An integer
    """
    def top(self):
        # write your code here

        if len(self.stack2) > 0:
            ret = self.stack2.pop()
            self.stack2.append(ret)
            return ret
        for i in range(len(self.stack1)):
            a = self.stack1.pop()
            self.stack2.append(a)

        ret = self.stack2.pop()
        self.stack2.append(ret)
        return ret





