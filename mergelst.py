def merge (nums1, nums2):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        l1 = len(nums1)
        l2 = len(nums2)
        i = 0
        j = 0
        k = []
        while i < l1 and j < l2:
        	if nums1[i] > nums2[j]:
        		k.append(nums1[i])
        		i += 1
        	else:
        		k.append(nums2[j])
        		j += 1
        if j == l2:
        	k.extend(nums1[i:])
        else:
        	k.extend(nums2[j:])
        return k
print(merge([100],[9,8,7,6,5,5,5,5,5,5]))
def climbStairs(n):
        """
        :type n: int
        :rtype: int
        """
        # if n < 0:
        #     return 0
        if n == 0 or n == 1:
            return 1

        else:
            return climbStairs(n-1) + climbStairs(n-2)
print(ord('a')-96)

def countPrimes(n):
        """
        :type n: int
        :rtype: int
        """
        d = [True]*(n-1)
        ct = 0
        for i in range(2,n-1):
            if d[i]:
                ct += 1
                j = i
                while i*j < n-1:
                    d[i*j] = False
                    j += 1
        return ct
# print(countPrimes(7))
from datetime import datetime
import re
response_time = "May 2, 2018 9:01"
def padd(time):
    day = re.search('(?P<month>.*) (?P<days>.*), (?P<year>.*) (?P<min>.*):(?P<res>.*)', time)
    days = int(day.group('days'))
    print(days)
    mins = int(day.group('min'))
    if days < 10:
        paddedday = "0" + day.group('days')
    else:
        paddedday = day.group('days')
    if mins < 10:
        paddedmin = "0" + day.group('min')
    else:
        paddedmin = day.group('min')
    padded = day.group('month') + " " + paddedday+ ", " + day.group('year') + " " + paddedmin + ":" + day.group('res')
    return padded
# print(days)
# print(mins)

print(padd(response_time))


def numSquares(n):

    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        factors = []
        i = 1
        while (i ** 2) <= n:
            factors.append(i ** 2)
            i += 1
        # print factors
        nm = {}
        for j in factors:
            nf = numSquares(n-j)
            nm[nf + 1] = j
        # print nm
        minn = min(nm.keys())
        fac = nm[minn]
        return minn
print(numSquares(42))

