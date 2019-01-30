s= "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    from collections import defaultdict
    dp = defaultdict(lambda: defaultdict(int))
    
    for i in range(len(s)):
        dp[i][i] = True
    
    
    for i in range(len(s)):
        for j in range(i):
            dp[i][j] = False
    for i in range(len(s)-1):
        dp[i][i+1] = (s[i] == s[i+1])
    # print dp
    
    for i in range(len(s)-2,-1,-1):
        for j in range(i+2,len(s)):
            # print i,j
            if (s[i] == s[j] and dp[i+1][j-1]) :
                # dp[i+1][j-1] == 0 and i+1 == j):
                dp[i][j] = True
            else:
                dp[i][j] = False
    # print dp
    ma = 0
    mai = 0
    maj = 0
    for i in dp:
        for j in dp[i]:
            if dp[i][j]:
                if j - i > ma:
                    ma = j - i
                    mai = i
                    maj = j
                
    return s[mai:maj+1]
s = "cbbd"
# print(longestPalindrome(s))


def findpoint(A, target):
    start = 0
    end = len(A) - 1
    while start + 1 < end: 
        mid = (start + end) / 2
        midval = A[mid]
        if midval > target:
            end = mid
        else:
            start = end
    if A[start] == target:
        return start
    elif A[end] == target:
        return end
    else:
        return start
# print(findpoint([1,4,5,6,7,10],))

    
def firstPosition(nums, target):
    if len(nums) == 0:
        return -1
    left = 0
    right = len(nums) -1
    
    while left + 1 < right:
        print left,right

        mid = (left + right) / 2
        midval = nums[mid]
        print midval
        if target <= midval:
            right = mid
        else:
            left = mid
    
    if nums[left] == target:
        return left  
    if nums[right] == target:
        return right
    return -1
# print(firstPosition([1,1,1,1,2,2,3,3,3,4,4,4,5,5,5,5,5,5],4))

def search(A, target):
    if len(A) == 0:
        return -1
    left = 0
    right = len(A) -1
   
    
    while left + 1 < right:
        print left, right
        mid = (left + right) / 2
        midval = A[mid]
        if A[-1] > midval:
            if target > midval and target <= A[right]:
                left = mid
            else:
                right = mid
        else:
            if target < midval and target >= A[left]:
                right = mid
            else:
                left = mid
    print(left,right)
    
    if A[right] == target:
        return right
    if A[left] == target:
        return left
    return -1
# print(search([6,8,9,1,3,5],5)) 


def findpoint(A, target):
    start = 0
    end = len(A) - 1
    while start + 1 < end: 
        mid = (start + end) / 2
        if A[mid] < target:
            start = mid
        else:
            end = mid
    if A[end] < target:
        return end
    if A[start] < target:
        return start
    
    return -1
print(findpoint([1,2,3],2))
print(sorted([3,4,5,6,4]))


def moveZeroes(nums):
        # write your code here
    nums.sort()
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j] = nums[i]
            j += 1
    for jj in range(j,len(nums)):
        nums[jj] = 0
    return nums
# print(moveZeroes([0,1,0,3,12]))


def twoSum(nums,target):
    # write your code here

    i = 0
    j = len(nums) - 1
    res = []
    while i <= j:
        if nums[i] + nums[j] > target:
            j -= 1
        elif nums[i] + nums[j] < target:
            i += 1
        else:
            while nums[i] == nums[i+1]:
                i += 1
            while nums[j] == nums[j-1]:
                j -= 1
            res.append([nums[i],nums[j]])
            i += 1
            j -= 1
            
    return res
print(twoSum([],6))


def threeSum(numbers):
        # write your code here
    numbers.sort()
    # print(numbers)
    sol = []
    for ii in range(0,len(numbers)-2):
        if (numbers[ii] == numbers[ii-1] and ii):
            continue
        left = ii + 1
        right = len(numbers) - 1
        target = -numbers[ii]
        sol.extend(twosumzero(numbers,left,right,target))
    return sol
        
    
        
# def twosumzero(nums,i,j,target):
#     # write your code here
#     res = []
#     while i < j:
#         if nums[i] + nums[j] == target:
#             res.append([-target,nums[i],nums[j]])
#             j -= 1
#             j += 1
            
#             while i < j and nums[i] == nums[i-1] :
#                 i += 1
#             while  i < j and nums[j] == nums[j+1]:
#                 j -= 1

#         elif nums[i] + nums[j] > target:
#             j -= 1
            
#         else:
#             i += 1
            
        
#     return res




# def threeSum(nums):
#     nums.sort()
#     res = []
#     length = len(nums)
#     for i in range(0, length - 2):
#         if i and nums[i] == nums[i - 1]:
#             continue
#         target = nums[i] * -1
#         left, right = i + 1, length - 1
#         res.extend(twosumzero(nums,left,right,target))

        
#     return res

def twosumzero(nums,left,right,target):
    res = []
    while left < right:
        if nums[left] + nums[right] == target:
            res.append([-target, nums[left], nums[right]])
            right -= 1
            left += 1
            while left < right and nums[left] == nums[left - 1]:
                left += 1
            while left < right and nums[right] == nums[right + 1]:
                right -= 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            left += 1
    return res


def threeSum(numbers):
    hashmap = {}
    sol = []
    adm = []
    for ii in numbers:
        if ii not in hashmap:
            hashmap[ii] = 1
        else:
            hashmap[ii] += 1
    for ii in range(1,len(numbers)):
        if numbers[ii] == numbers[ii-1]:
            continue
        res = find(hashmap,-numbers[ii])
        for kk in res:
            if set(kk) not in adm:
                adm.append(set(kk))
                sol.append(kk)
    return sol
            
            
    
def find(hashmap,value):
    ret = []
    for ii in hashmap:
        if value - ii in hashmap:
            if ii != value - ii:
                ret.append([-value, ii,value-ii])
            elif ii == value - ii:
                if hashmap[ii] > 1:
                    ret.append([-value,ii,value-ii])
            elif ii == value:
                print("hh")
                if hashmap[ii] > 1:
                    ret.append([-value,ii,value-ii])
            elif value - ii == value:
                print("hh")
                if hashmap[value - ii] > 1:
                    ret.append([-value,ii,value-ii]) 

    return ret

print(threeSum([-2,-3,-4,-5,-100,99,1,4,4,4,5,1,0,-1,2,3,4,5]))
print(threeSum([-1,1,0]))
print(len(threeSum([-2,-3,-4,-5,-100,99,1,4,4,4,5,1,0,-1,2,3,4,5])))
print(len([[-100,1,99],[-5,0,5],[-5,1,4],[-5,2,3],[-4,-1,5],[-4,0,4],[-4,1,3],[-3,-2,5],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-2,1,1],[-1,0,1]]))



def canFinish(numCourses, prerequisites):
        # Write your code here
    edges = {i: [] for i in xrange(numCourses)}
    degrees = [0 for i in xrange(numCourses)] 
    for i, j in prerequisites:
        edges[j].append(i)
        degrees[i] += 1
    import Queue
    queue, count = Queue.Queue(maxsize = numCourses), 0
    
    for i in xrange(numCourses):
        if degrees[i] == 0:
            queue.put(i)

    while not queue.empty():
        node = queue.get()
        count += 1

        for x in edges[node]:
            degrees[x] -= 1
            if degrees[x] == 0:
                queue.put(x)



    return count == numCourses





start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log",'cog']
import string

def ladderLength(start, end, dict):
        # write your code here
    length = 0
    queue = [start]
    while queue:
        length += 1
        head = queue.pop(0)
        for jj in range(len(head)):
            newstr = head
            for ii in list(string.ascii_lowercase):
                newstr = changechar(newstr,jj,ii)
                if newstr == end:
                    return length
                if newstr in dict:
                    queue.append(newstr)

    return -1
    
def changechar(s,i,rep):
    ss = list(s)
    ss[i] = rep
    ret = "".join(ss)
    return ret
print(ladderLength(start, end, dict))

import collections



start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]

def ladderLength(self, start, end, dict):
        # write your code here
    dict.add(end)
    wordLen = len(start)
    queue = collections.deque([(start, 1)])
    while queue:
        curr = queue.popleft()
        currWord = curr[0]; currLen = curr[1]
        if currWord == end: return currLen
        for i in xrange(wordLen):
            part1 = currWord[:i]; part2 = currWord[i+1:]
            for j in 'abcdefghijklmnopqrstuvwxyz':
                if currWord[i] != j:
                    nextWord = part1 + j + part2
                    if nextWord in dict:
                        queue.append((nextWord, currLen + 1))
                        dict.remove(nextWord)
    return 0
# print(ladderLength(start,end,dict))


def findMin(nums):
        # write your code here
        
    A = nums
    start = 0
    end =  len(A) - 1
    while start + 1  < end:
        mid =(start + end) // 2
        midval = A[mid]
        if  midval < A[end]:
            end = mid
        else:
            start = mid
    
    return min(A[end],A[start])
print(findMin([1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1]))
