
"""
Trap rain water
"""

"""
整个算法的思想是计算每个位置上可以盛放的水，累加起来。

记录如下几个值：

left, right => 左右指针的位置
left_max, right_max => 从左到右和从右到左到 left, right 为止，找到的最大的 height
每次比较 left_max 和 right_max，如果 left_max 比较小，就挪动 left 到 left + 1。
与此同时，查看 left 这个位置上能够盛放多少水，这里有两种情况：

1.一种是 left_max > heights[left]，这种情况下，水可以盛放 left_max - heights[left] 那么多。因为右边有 right_max 挡着，左侧可以到 left_max。

2.一种是 left_max <= heights[left]，这种情况下，水无法盛放，会从左侧流走，此时更新 left_max 为 heights[left]

left_max >= right_max 的情况类似处理。
"""

class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """

    def trapRainWater(self, heights):
        if not heights:
            return 0
        left = 0
        right = len(heights) - 1
        leftmax = heights[left]
        rightmax = heights[right]
        
        water = 0
        while left <= right:
            if leftmax < rightmax:
                if leftmax > heights[left]:
                    water += leftmax - heights[left]
                else:
                    leftmax = heights[left]
                left += 1
                
                
            else:
                if rightmax > heights[right]:
                    water += rightmax - heights[right]
                else:
                    rightmax = heights[right]
                right -= 1
                
        return water

"""
Implement Queue by Two Stacks 

"""
"""
Queue with 2 stacks
1.  现在我们已经有了两个栈stack1和stack2，最暴力的做法，当需要往队列中加入元素时，
可以往其中一个栈stack2中加入元素，当需要得到队头元素时，只需要将stack2中的元素倒入到stack1中，
再取stack1的头元素就可以了，如果是需要删掉队头元素，那么直接pop stack1的栈顶元素就可以了，
再将stack1中的元素再倒入到stack2中，以便下一次的加入元素


2.  上面的实现中，我们每取一次队头元素或者删掉队头元素，我们都需要将stack2中的元素先倒入到stack1中，
再从stack1中倒回去，每次需要倒两边十分麻烦，那么是否有更加简便一些的方法呢？答案当然是有的，
其实当我们将stack2中的元素倒入到stack1中的时候，我们发现stack1中的元素的顺序就是按照队列的先进先出顺序，
那么我们不再将stack1中的元素倒入到stack2中，在获取队头元素或者删除队头元素的时候，
我们先判断stack1是否为空，如果不为空，从stack1中取即可，如果为空，那么将stack2中的元素倒入到stack1中，
每次加入元素的时候都是往stack2中加入元素。
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





