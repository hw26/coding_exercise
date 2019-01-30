def canPartition( nums):
        
    # write your code here
    if combinationSum2(nums,float(sum(nums))/2) != []:
        return True
    return False
def combinationSum2( num, target):
    # write your code here
    if len(num) == 0:
        return []
    results = []
    subset = []
    num.sort()

    helper(num,target,0,subset,results)
    return results
    
def helper(nums,target_remain,startIdx, subset,results):
    
    
        
    if target_remain == 0:
        if subset not in results:
            results.append(list(subset)) 
    for ii in xrange(startIdx,len(nums)):
        if target_remain-nums[ii] <0:
            break
        if nums[ii] == nums[ii-1] and ii > startIdx:
            continue
        subset.append(nums[ii])
        helper(nums,target_remain-nums[ii],ii+1,subset,results)
        subset.pop(len(subset)-1)
# print(canPartition([26,50,29,47,43,80,10,65,59,23,71,83,29,40,92,9,90,46,20,2,41,30,38,71,83,37,93,51,62,16,56,84,83,36,91,62,42,53,84,77,97,22,98,99,86,31,95,67,57,16,96,76,82,44,91,94,28,8,90,17,6,53,70,6,45,21,37,51,51,20,4,53,72,80,58,20,5,30,63,81,22,73,35,77,90,23,83,13,75,74,91,83,53,97,76,64,94,36,84,10,85,98,24,14,95,58,54,80,90,73,39,100,65,39,18]))
import math
def helper(remain):
    results = []
    for ii in xrange(2,int(remain)/2+1):
        if remain % ii == 0:
            results.append(ii)
            remain /= ii
            if remain == 0:
                break
    # results.append(remain)
    return results
print(helper(81))

def nextClosestTime(time):
        # write your code here
    digits = []
    for ii in range(len(time)):
        if  time[ii] != ":":
            digits.append(int(time[ii]))
    # digits.extend(digits)

    print(digits)
    print(permuteUnique(digits))

def permuteUnique( nums):
    # write your code here
    results = []
    if len(nums) == 0:
        return [[]]
    nums.sort()
    helper(nums,[],[False for i in range(len(nums))],results)
    
    return results
    
def helper(nums,permutation,visited,results):
    
    if len(permutation) == 4:
        results.append(list(permutation))
    for ii in range(len(nums)):
        if visited[ii]:
            continue
        if ii > 0 and nums[ii] == nums[ii-1] and not visited[ii-1]:
            continue
        permutation.append(nums[ii])
        visited[ii] = True
        helper(nums,permutation,visited,results)
        visited[ii] = False
        permutation.pop(len(permutation)-1)
# print(nextClosestTime("13:24"))



def findLadders(self, start, end, dict):
        # write your code here
        ## dfs and BFS together
    dict.add(end)
    distances = self.finddistance(end,dict)
    results = []
    self.dfspaths([start],end,distances,results)
    return results
    
    
def dfspaths(self,path,end,distances,results):
    print path[-1]
    if path[len(path)-1] == str(end):
        results.append(list(path))
        # print(results)
    end = path[-1]
    for ii in self.changecharlist(end):
        if ii in distances:
            
            if distances[ii] == distances[end] - 1:
                path.append(ii)
                self.dfspaths(path,end,distances,results)
                path.pop(len(path)-1)
    
    
    
    
def finddistance(self,end,dicter):
    q = [end]
    visited = set([end])
    dist = {end:0}
    while q:
        head = q.pop(0)
        for ii in self.changecharlist(head):
            if ii in dicter:
                if ii not in visited:
                    dist[ii] = dist[head] + 1
                    visited.add(ii)
    return dist
def changecharlist(self,string):
    res = []
    for ii in range(len(string)):
        for jj in "qwertyuiopasdfghjklzxcvbnm":
            st = list(string)
            if st[ii] != jj:
                st[ii] = jj
                res.append(("").join(st))
        return res


from heapq import heappush,heappop,heapify

h = []

### push
heappush(h, 5)
heappush(h, 7)
heappush(h, 1)
heappush(h, 3)
heappush(h, 31)
heappush(h, 5)
heappush(h, 6)

### pop smallest
a = heappop(h)
print(a)

### peek
b = h[0]
print(b)

### delete ith element
h[2] = h[-1]
h.pop()
heapify(h)
print(h)



a= [(2,4),(12,17),(18,21),(23,25),(40,42),(51,54),(58,59),(63,67),(77,78),(84,88),(89,92),(97,111),(121,125),(129,133),(138,140),(149,152),(155,158),(175,177),(182,185),(188,192),(196,218),(223,226),(228,231),(234,237),(259,265),(271,274),(276,282),(287,288),(299,300),(301,303),(304,308),(314,317),(318,323),(327,331),(333,342),(345,357),(358,360),(362,365),(367,375),(376,382),(386,404),(413,414),(418,421),(423,432),(434,436),(439,442),(445,448),(450,454),(457,459),(464,465),(483,484),(493,501),(504,506),(533,534),(539,541),(551,554),(557,565),(566,568),(575,587),(588,594),(603,604),(611,625),(632,633),(634,647),(649,655),(665,675),(683,685),(694,698),(706,708),(711,714),(719,721),(724,726),(737,746),(753,756),(770,785),(796,809),(810,811),(814,828),(833,835),(840,848),(851,852),(853,855),(857,865),(866,868),(870,871),(874,875),(878,881),(882,885),(898,900),(902,907),(921,924),(936,946),(947,948),(952,957),(959,965),(966,967),(972,975),(976,982),(985,986),(987,988)]
b = [(3,16),(17,20),(23,28),(34,42),(46,58),(62,64),(65,68),(75,76),(79,82),(85,88),(92,96),(99,100),(101,108),(110,117),(119,120),(121,126),(127,130),(134,136),(137,143),(145,146),(147,156),(175,182),(186,187),(199,207),(214,221),(227,239),(248,257),(259,265),(271,280),(283,285),(291,293),(314,319),(322,326),(342,343),(346,348),(350,352),(356,360),(383,393),(394,411),(412,418),(428,431),(432,439),(443,445),(456,458),(460,478),(488,493),(497,498),(499,505),(506,510),(512,514),(532,534),(536,547),(561,562),(568,569),(571,572),(580,582),(584,592),(594,596),(605,610),(628,636),(637,641),(644,649),(653,657),(665,667),(673,674),(679,682),(683,684),(685,687),(688,693),(696,698),(700,703),(705,718),(720,721),(728,729),(730,734),(738,742),(746,757),(759,761),(765,768),(770,790),(796,798),(802,805),(815,832),(836,844),(864,865),(874,875),(878,881),(884,887),(888,890),(896,897),(898,901),(903,905),(909,915),(916,928),(930,940),(944,951),(952,957),(960,963),(969,990),(991,1000)]
"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param list1: one of the given list
    @param list2: another list
    @return: the new sorted list of interval
    """
    def mergeTwoInterval(self, list1, list2):
        ans = [(0,-float('inf'))]
        i = 0
        j = 0
        
        while i < len(list1) and j <len(list2):
            last = ans[-1]
            int1 = list1[i]
            int2 = list2[j]
            if int1[0] < int2[0]:
                if int1[0] <= last[1]:
                    laster = (last[0],max(last[1],int1[1]))
                    ans[-1] = laster
                else:
                    ans.append(int1)
                i += 1
            else:
                if int2[0] <= last[1]:
                    laster = (last[0],max(last[1],int2[1]))
                    ans[-1] = laster
                else:
                    ans.append(int2)
                j += 1

                    
                
        if i == len(list1):
            ans.extend(list2[j:])
        elif j == len(list2):
            ans.extend(list1[i:])
        return ans[1:]

# sol = Solution()
# print(sol.mergeTwoInterval(a,b))
                
# ans = [(2,21),(23,28),(34,42),(46,59),(62,68),(75,76),(77,78),(79,82),(84,88),(89,96),(97,117),(119,120),(121,126),(127,133),(134,136),(137,143),(145,146),(147,158),(175,185),(186,187),(188,192),(196,221),(223,226),(227,239),(248,257),(259,265),(271,282),(283,285),(287,288),(291,293),(299,300),(301,303),(304,308),(314,326),(327,331),(333,343),(345,360),(362,365),(367,375),(376,382),(383,411),(412,421),(423,442),(443,448),(450,454),(456,459),(460,478),(483,484),(488,510),(512,514),(532,534),(536,547),(551,554),(557,565),(566,569),(571,572),(575,596),(603,604),(605,610),(611,625),(628,657),(665,675),(679,682),(683,687),(688,693),(694,698),(700,703),(705,718),(719,721),(724,726),(728,729),(730,734),(737,757),(759,761),(765,768),(770,790),(796,809),(810,811),(814,832),(833,835),(836,848),(851,852),(853,855),(857,865),(866,868),(870,871),(874,875),(878,881),(882,887),(888,890),(896,897),(898,901),(902,907),(909,915),(916,928),(930,951),(952,957),(959,965),(966,967),(969,990),(991,1000)]
# my = [(2, 21), (23, 28), (34, 42), (46, 59), (62, 68), (75, 76), (77, 78), (79, 82), (84, 88), (89, 96), (97, 117), (119, 120), (121, 126), (127, 133), (134, 136), (137, 143), (145, 146), (147, 158), (175, 185), (186, 187), (188, 192), (196, 221), (223, 226), (227, 239), (248, 257), (259, 265), (271, 282), (283, 285), (287, 288), (291, 293), (299, 300), (301, 303), (304, 308), (314, 326), (327, 331), (333, 343), (345, 360), (362, 365), (367, 375), (376, 382), (383, 411), (412, 421), (423, 442), (443, 448), (450, 454), (456, 459), (460, 478), (483, 484), (488, 510), (512, 514), (532, 534), (536, 547), (551, 554), (557, 565), (566, 569), (571, 572), (575, 596), (603, 604), (605, 610), (611, 625), (628, 657), (665, 675), (679, 682), (683, 687), (688, 693), (694, 698), (700, 703), (705, 718), (719, 721), (724, 726), (728, 729), (730, 734), (737, 757), (759, 761), (765, 768), (770, 790), (796, 809), (810, 811), (814, 832), (833, 835), (836, 848), (851, 852), (853, 855), (857, 865), (866, 868), (870, 871), (874, 875), (878, 881), (882, 887), (888, 890), (896, 897), (898, 901), (902, 907), (909, 915), (916, 928), (930, 951), (952, 957), (959, 965), (966, 967), (969, 990), (991, 1000)]
# print(ans == my)


class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        prefixsum = [0 for i in range(len(nums))]
        for ii in range(1,len(nums)):
            prefixsum[ii] = prefixsum[ii-1] + nums[ii]
        for ii in range(len(nums)):
            for jj in range(ii+1,len(nums)):
                if prefixsum[ii] == prefixsum[jj]:
                    return [ii,jj]
sol = Solution()
print(sol.subarraySum([-3,1,2,-3,4]))


def gte(nums,x):
        # returns the number of elements gte than x in nums
    start = 0
    end = len(nums)-1
    count = 0
    while start + 1 < end:
        mid = (start + end) / 2
        midval = nums[mid]
        if midval >= x:
            end = mid
        else:
            start = mid
    if nums[start] >= x:
        return len(nums) - start
    elif nums[end] >= x and x > nums[start]:
        return len(nums) - end
        
    return 0
print(gte([1,2,3],3))
