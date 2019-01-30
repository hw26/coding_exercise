def tupleMultiply(tuple, n):
        # Write your code here
    if n >= 3:
        return None
    tuplearr = []
    ii = 0
    while ii < len(tuple):

        if unicode(tuple[ii]).isnumeric():
            num = tuple[ii]
            while ii + 1 < len(tuple) and unicode(tuple[ii+1]).isnumeric():
                num += tuple[ii]
                ii += 1
            tuplearr.append(num)
        
    	ii += 1
    print(tuplearr)

# def isnumeric(st):
#     a = range(10)
#     return int(st)
tupleMultiply("(1,2,3),(4,500,6),(7,8,9800)",2)

# def getSingleNumber(nums):
#     index = 0
#     for ii in range(len(nums)-1):
#         if nums[index] == nums[ii]:
#             index += 1
#     print index
# getSingleNumber([1,2,2,3,3])\\\

class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    def largestRectangleArea(self, heights):
        indices_stack = []
        area = 0
        for index, height in enumerate(heights + [-1]):
            while indices_stack and heights[indices_stack[-1]] >= height:
                popped_index = indices_stack.pop()
                left_index = indices_stack[-1] if indices_stack else -1
                width = index - left_index - 1
                area = max(area, width * heights[popped_index])
                
            indices_stack.append(index)
            
        return area
sol = Solution()
print(sol.largestRectangleArea([2,1,5,3,2]))


def lastPosition(nums, target):
        ## find the last position that is smaller than target
    if len(nums) == 0:
        return -1
    left = 0
    right = len(nums) -1
    
    while left + 1 < right:
        mid  = (left + right) /2
        if nums[mid] < target:
            left = mid
        elif nums[mid] > target:
            right = mid
        else:
            right = mid
    
    if nums[right] <= target:
        return right
    
    return left
print(lastPosition([1,2,3,4,5],4))


def twoSumzero(nums,target):
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
print((twoSumzero([1,2,3,4,4,5,6,6,6],9)))

class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        numbers.sort()
        sol = []
        for ii in range(len(numbers)):
            

            res = self.twoSumzero(numbers[:ii],-numbers[ii])
            if numbers[ii] == 1:
                print(res)
            for item in res:
                solp = item + [numbers[ii]]
                solp.sort()
                if solp not in sol:
                    sol.append(solp)
            
        return sol
            
        
            
    def twoSumzero(self, nums,target):
        # write your code here
        i = 0
        j = len(nums) - 1
        res = []
        while i < j:
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
sol = Solution()
print(sol.threeSum([-2,-3,-4,-5,-100,99,1,4,4,4,5,1,0,-1,2,3,4,5]))


def deduplication( nums):
        # write your code here
    nums.sort()
    j = 0
    for i in range(len(nums)-1):
        if nums[i] != nums[i+1]:
            nums[j] = nums[i]
            j += 1
    return j,nums

print(deduplication([1,3,1,4,4,2]))



111
a = [446,242,400,308,858,680,290,597,418,552,810,890,452,374,425,412,490,732,397,231,138,923,204,163,685,406,134,530,814,776,115,827,902,75,875,756,570,648,420,420,883,788,254,251,189,551,917,451,637,897,867,391,272,447,709,346,371,503,886,566,985,460,78,330,581,256,182,345,278,137,912,170,233,707,652,1000,201,231,82,932,263,471,739,61,904,571,818,238,544,706,889,974,86,617,871,930,223,184,73,109,86,985,197,535,974,298,594,771,130,178,171,725,449,577,740,152,588,239,617,784,404,319,795,84,906,773,808,578,699,717,222,386,677,390,976,967,658,130,129,108,473,948,623,902,524,587,588,732,968,887,821,607,163,180,524,758,337,270,153,723,242,929,470,88,830,467,944,588,623,912,892,635,946,650,941,310,674,207,343,984,896,760,152,293,311,169,983,53,581,626,606,806,119,440,348,68,198,651,493,191,90,238,828,179,431,332,156,587,960,444,499,792,822,418,53,870,746,456,724,546,388,829,885,740,306,396,439,256,123,119,768,949,288,192,998,955,592,509,106,89,586,107,639,166,411,611,275,166,923,579,608,588,770,488,688,754,445,209,334,642,405,587,635,786,928,984,787,739,600,857,268,905,872,577,878,644,819,421,893,290,610,283,831,581,376,596,583,83,101,68,925,304,371,713,912,765,346,1000,489,990,978,865,791,202,937,855,886,496,654,590,336,63,588,233,86,917,220,928,221,655,465,818,595,968,81,791,289,866,454,986,852,742,377,94,787,74,992,388,973,621,451,83,849,947,480,862,393,938,746,685,69,669,537,907,714,899,705,408,743,595,846,408,942,375,263,804,695,777,253,317,820,939,915,619,916,796,887,76,588,843,847,408,612,563,733,864,882,398,953,882,635,980,779,882,145,476,605,424,304,265,565,474,73,1000,835,732,537,889,639,930,648,763,207,201,123,761,119,599,420,332,984,886,857,211,642,518,269,840,355,450,795,85,873,734,501,963,56,186,426,275,606,86,341,738,599,64,76,411,485,961,818,303,659,277,997,850,108,375,631,748,478,436,657,812,862,689,959,674,445,388,973,545,879,437,918,409,783,484,736,227,466,169,348,285,377,112,780,977,678,840,826,830,92,232,937,890,542,230,208,668,725,289,673,670,178,861,316,712,148,683,450,757,649,672,605,569,314,179,959,715,605,824,842,428,586,590,833,280,990,412,349,154,503,426,91,148,759,257,408,344,670,462,738,83,906,644,911,689,811,284,739,521,935,737,355,995,109,734,685,104,328,356,610,385,562,726,809,588,898,266,769,790,571,347,841,189,304,738,352,449,439,952,766,394,890,368,848,845,540,495,856,332,882,762,929,470,409,158,118,799,263,622,124,787,709,428,880,768,948,856,586,775,562,705,145,609,435,566,429,230,459,992,465,350,485,63,825,101,483,980,72,464,663,134,462,791,806,589,812,803,684,208,927,938,688,844,434,630,175,867,828,371,333,464,382,164,523,784,978,491,558,277,811,388,384,590,828,486,855,237,719,90,164,665,995,163,551,524,264,417,407,245,672,848,251,815,572,912,964,156,105,256,306,151,331,956,57,393,374,459,212,813,401,845,312,794,879,456,398,942,630,206,654,369,119,718,664,704,547,471,824,692,456,176,947,369,899,149,161,144,723,705,578,223,969,634,565,135,846,765,743,850,409,846,399,280,820,596,556,730,75,179,998,746,868,619,387,980,343,988,368,75,261,388,956,133,394,778,185,897,143,767,518,284]
class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        # write your code here
        # dp[i][c] = max weight to fill with capacity c and bags i ... n-1
        dp = [[0 for _ in range(m+1)] for _ in range(len(A))]
        for ii in range(len(A)):
            dp[ii][0] = 0
        for cc in range(m+1):
            if A[len(A)-1] <= cc:
                dp[len(A)-1][cc] = A[len(A)-1]
            else:
                dp[len(A)-1][cc] = 0
                
        # print(dp)
            
        for ii in range(len(A)-2,-1,-1):
            for c in range(m+1):
                if c - A[ii] >= 0:
                    dp[ii][c] = max(dp[ii+1][c-A[ii]] + A[ii],dp[ii+1][c])
                else:
                    dp[ii][c] = dp[ii+1][c]

        return dp[0][m]

# sol = Solution()
# print(sol.backPack(80000,a))


class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, dict):
        # write your code here
        if not s and not dict:
            return True
        memo = {}
        
        return self.helper(s,memo,dict)
        
    def helper(self,s,memo,wordDict):

        if s in memo:
            return memo[s]
        if len(s) == 0:
            return True
        memo[s] = False
        if s in wordDict:
            memo[s] = True
            return True
        
        for i in range(len(s)):
            # print(s[:i+1] in wordDict)
            if s[:i+1] not in wordDict:
                continue
            
            postfix = self.helper(s[i+1:],memo,wordDict)
            print(s[i+1:])
            print(postfix)
            if postfix:
                memo[s] = postfix
        return memo[s]
sol = Solution()
print(sol.wordBreak("abcd",["a","b","abc","cd"]))


    
def findsubarray(n):
    if n == 1:
        return [[1]]
    else:
        res = []
        for subset in findsubarray(n-1):
            if subset[-1] == n - 1:
                res.append(list(subset+[n]))
                res.append(list(subset))
            else:
                res.append(list(subset))
        res.append([n])
        return res
print(findsubarray(5))