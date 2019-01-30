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
        
        return self.helper(s,dict)
        
    def helper(self,s,wordDict):

        
        if len(s) == 0:
            
            return True

        res = False
        if s in wordDict:
            return True
        
        for i in range(len(s)):
            if s[:i+1] not in wordDict:
                continue
            
            postfix = self.helper(s[i+1:],wordDict)
            if postfix:
                res = True
                break
        return res

a = Solution()
print(a.wordBreak("lintcodehello",["lint","code","hello"]))