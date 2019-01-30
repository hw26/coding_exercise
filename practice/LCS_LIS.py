"""-------------------------------------------Longest Common Subsequence-------------------------------------------"""


class Solution:
    """
    @param A: A string
    @param B: A string
    @return: The length of longest common subsequence of A and B
    """
    def longestCommonSubsequence(self, A, B):
        n, m = len(A), len(B)
        f = [[0] * (m + 1), [0] * (m + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if A[i - 1] == B[j - 1]:
                    f[i % 2][j] = f[(i - 1) % 2][j - 1] + 1
                else:
                    f[i % 2][j] = max(f[i % 2][j - 1], f[(i - 1) % 2][j])
        return f[n % 2][m]


class Solution:
    """
    @param P: an integer array P
    @param Q: an integer array Q
    @param k: the number of allowed changes
    @return: the length of lca with at most k changes allowed.
    """
    def longestCommonSubsequence2(self, P, Q, k):
        # Write your code here
        m = len(P)
        n = len(Q)
        l = [[[None for g in range(k+1)] for j in range(n+1)] for i in range(m+1)]
        # l = length of LCS with K changes performed
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    l[i][j][0] = 0
                elif P[i-1] == Q[j-1]:
                    l[i][j][0] = l[i-1][j-1][0] + 1
                else:
                    l[i][j][0] = max(l[i-1][j][0], l[i][j-1][0])
        for i in range(m+1):
            for j in range(n+1):
                for g in range(1, k+1):
                    if i == 0  or j == 0:
                        l[i][j][g] = 0
                    elif P[i-1] != Q[j-1]:
                        l[i][j][g] = max(l[i-1][j][g], l[i][j-1][g], l[i-1][j-1][g-1] + 1)
                    else:
                        l[i][j][g] = max(l[i-1][j][g], l[i][j-1][g], l[i-1][j-1][g] + 1)
        return l[m][n][k]

"""-------------------------------------------Longest Common Substring-------------------------------------------"""


def LCSubStr(X, Y): 
      

    m = len(X)
    n = len(Y)
    dp = [[0 for k in range(n+1)] for l in range(m+1)] 
      
    # To store the length of  
    # longest common substring 
    result = 0 
  
    # Following steps to build 
    # LCSuff[m+1][n+1] in bottom up fashion 
    for i in range(m + 1): 
        for j in range(n + 1): 
            if (i == 0 or j == 0): 
                dp[i][j] = 0
            elif (X[i-1] == Y[j-1]): 
                dp[i][j] = dp[i-1][j-1] + 1
                result = max(result, dp[i][j]) 
            else: 
                dp[i][j] = 0
    return result 

# print(LCSubStr("hello","bhhfhellother"))






"""-------------------------------------------Longest Increasing Subsequence-------------------------------------------"""





class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        # write your code here
        if nums is None or not nums:
            return 0
        dp = [1] * len(nums)
        for curr in range(len(nums)):
            val = nums[curr]
            for prev in range(curr):
                if nums[prev] < val:
                    dp[curr] = max(dp[curr], dp[prev] + 1)
        return max(dp)

a = Solution()
print(a.longestIncreasingSubsequence([1,2,3,4,6,5]))



class Solution:
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        #state and init
        f = [1] * len(nums)
        ans = [1] * len(nums)
        #func
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    if f[j] + 1 > f[i]:
                        ans[i] = ans[j]
                        f[i] = f[j] + 1
                    elif f[j] + 1 == f[i]:
                        ans[i] += ans[j]
        #ans
        res = sum(y for x, y in zip(f, ans) if x == max(f))
        return res
