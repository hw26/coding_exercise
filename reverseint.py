

def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    res = ''
    if x == 0:
        return '0'
    for i in str(x):
        res = i + res
    ret = str(res) 
    # print ret
    j = 0
    while res[j] == '0':
        j += 1
    ret = ret[j:]
    if ret[-1] == '-':
        ret = "-"+ ret[:-1]
    return ret
print(reverse(100))

def plusOne(digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[len(digits)-1] < 9:
            digits[len(digits)-1] += 1
            return digits
        else:
            j = len(digits)-1
            while j >= 0:
                if digits[j] == 9:
                    j -= 1
            if j < 0:
                digits = [1] + [0]*len(digits)
            else:
                digits[j] += 1
                for k in range(j,len(digits)):
                    digits[k] = 0
            return digits
# print(plusOne([8,9,9,9]))
from collections import defaultdict
def longestPalindrome(s):
    dp = defaultdict(lambda: defaultdict(int))
    
    for i in range(len(s)):
        dp[i][i] = 1
    
    for i in range(len(s)):
        for j in range(i):
            dp[i][j] = 0
    
    for i in range(len(s)-2,-1,-1):
        for j in range(i+1,len(s)):
            if s[i] == s[j]:
                if dp[i+1][j-1] != 0 or (dp[i+1][j-1] == 0 and i+1 == j):
                    dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = 0
    ma = 0
    for i in dp:
        for j in dp[i]:
            ma = max(ma,dp[i][j])
    for i in dp:
        for j in dp[i]:
            if ma == dp[i][j]:
                return s[i:j+1]


def longestPalindrome(s):
        if len(s)==0:
            return 0
        maxLen=1
        start=0
        for i in xrange(len(s)):
            if i-maxLen >=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
                start=i-maxLen-1
                maxLen+=2
                continue

            if i-maxLen >=0 and s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
                start=i-maxLen
                maxLen+=1
        return s[start:start+maxLen]
print(longestPalindrome("whdqcudjpisufnrtsyupwtnnbsvfptrcgvobbjglmpynebblpigaflpbezjvjgbmofejyjssdhbgghgrhzuplbeptpaecfdanhlylgusptlgobkqnulxvnwuzwauewcplnvcwowmbxxnhsdmgxtvbfgnuqdpxennqglgmspbagvmjcmzmbsuacxlqfxjggrwsnbblnnwisvmpwwhomyjylbtedzrptejjsaiqzprnadkjxeqfdpkddmbzokkegtypxaafodjdwirynzurzkjzrkufsokhcdkajwmqvhcbzcnysrbsfxhfvtodqabvbuosxtonbpmgoemcgkudandrioncjigbyizekiakmrfjvezuzddjxqyevyenuebfwugqelxwpirsoyixowcmtgosuggrkdciehktojageynqkazsqxraimeopcsjxcdtzhlbvtlvzytgblwkmbfwmggrkpioeofkrmfdgfwknrbaimhefpzckrzwdvddhdqujffwvtvfyjlimkljrsnnhudyejcrtrwvtsbkxaplchgbikscfcbhovlepdojmqybzhbiionyjxqsmquehkhzdiawfxunguhqhkxqdiiwsbuhosebxrpcstpklukjcsnnzpbylzaoyrmyjatuovmaqiwfdfwyhugbeehdzeozdrvcvghekusiahfxhlzclhbegdnvkzeoafodnqbtanfwixjzirnoaiqamjgkcapeopbzbgtxsjhqurbpbuduqjziznblrhxbydxsmtjdfeepntijqpkuwmqezkhnkwbvwgnkxmkyhlbfuwaslmjzlhocsgtoujabbexvxweigplmlewumcone"))



def divide(dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    if dividend == 0:
        return 0
    elif dividend == divisor:
        return 1
    elif dividend * divisor > 0:
        quotient = 0
        if divisor < 0:
            while dividend < 0:
                
                # print(dividend)
                # print(quotient)
                dividend -= divisor
                quotient += 1
                if dividend == 0:
                    return quotient
                elif dividend > 0:
                    return quotient + 1
        else:
            while dividend > 0:
            
            # print(dividend)
            # print(quotient)
                dividend -= divisor
                quotient += 1
                if dividend == 0:
                    return quotient
                elif dividend < 0:
                    return quotient-1
                
            
        
    elif divisor < 0:
        quotient = 0
        while dividend > 0:
            dividend += divisor
            quotient -= 1
            if dividend == 0:
                return quotient
            elif dividend < 0:
                return quotient + 1
            
    elif dividend < 0:
        quotient = 0
        while dividend < 0:
            dividend += divisor
            quotient -= 1
            if dividend == 0:
                return quotient
            elif dividend > 0:
                return quotient + 1
print(divide(-2147,-1))


def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    if n == 1:
        return ["()"]
    else:
        resset = set([])
        for i in generateParenthesis(n-1):
            resset.add("()"+i)
            resset.add("("+i+")")
            resset.add(i+"()")
        return resset
print(generateParenthesis(3))

a = ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
b = ["()()()()","(()()())","()(()())","((()()))","(()())()","()()(())","(()(()))","()(())()","()((()))","(((())))","((()))()","((())())","(())()()"]
for aa in a:
    if aa not in b:
        print(aa)

str = "www.googel.com/count=134"
import re
print(re.findall(r'\d+', str))
