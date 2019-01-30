class Solution:
    """
    @param s1: a string
    @param s2: a string
    @return: is s1 and s2 are equivalent
    """
    def isEquivalentStrings(self, s1, s2):
        # Write your code here
        return self.helper(s1,s2)
        
    def helper(self,s1,s2):
        if s1 == s2:
            return True
        if len(s1) == len(s2) and len(s1) == 1:
            return s1 == s2
        if len(s1) == len(s2) and len(s1) == 2:
            return s1 == s2 or (s1[0] == s2[1] and s1[1] == s2[0])
        a1 = s1[:len(s1)//2]
        b1 = s2[:len(s2)//2]
        a2 = s1[len(s1)//2+1:]
        b2 = s2[len(s1)//2+1:]
        return self.helper(a1,b2) and self.helper(a2,b1)


sol = Solution()
print(sol.isEquivalentStrings("aa","ab"))


class Solution:
    """
    @param s: A string
    @return: An integer
    """
    def minCut(self, s):
        if len(s)== 1 or len(s) == 0:
            return 0
        matrix = self.getisPalindromematrix(s)
        precount = 0
        res = []
        self.helper(s,0,precount,matrix,res)
        return min(res)-1
        # return precount
        
    def helper(self,s,startIdx,precount,matrix,res):
        ### returns the number of palindrom partitions that can be made from startIdx to n-1
        if startIdx == len(s):
            return res.append(precount)
        for i in range(startIdx,len(s)):
            if not self.getisPalindrome(s,startIdx,i,matrix):
                continue
            precount += 1
            self.helper(s,i+1,precount,matrix,res)
            precount -= 1

    
    def getisPalindrome(self,s,startIdx,endIdx,matrix):
        return matrix[startIdx][endIdx]
        
    def getisPalindromematrix(self,s):
        mat = [[False for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)):
            mat[i][i] = True
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                mat[i][i+1] = True
        for i in range(len(s) - 3,-1,-1):
            for j in range(i+2,len(s)):
                mat[i][j] = mat[i+1][j-1] and s[i] == s[j]
        return mat



st = "ababababababababababababcbabababababababababababa"

hh = Solution()
# print(hh.minCut(st))