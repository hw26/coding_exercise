class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        dicter = {}
        count = {}

        for num in nums:
            dicter[num] = {}
            count[num] = 0
        for num1 in nums:
            count[num1] += 1


        for ind in range(len(nums)):
            n = nums[ind]
            for other in self.find_others(nums,ind):
                dicter[n][other] = 0 - other - n

        setter = []
        for num1 in dicter:
            for num2 in dicter[num1]:
                if dicter[num1][num2] in nums:
                    if num1 == num2:
                        if count[num1] >= 2:
                            if set([num1,num2,dicter[num1][num2]]) not in setter:
                                setter.append(set([num1,num2,dicter[num1][num2]]))
                                res.append([num1,num2,dicter[num1][num2]])
                    elif num1 == dicter[num1][num2]:
                        if count[num1] >= 2:
                            if set([num1,num2,dicter[num1][num2]]) not in setter:
                                setter.append(set([num1,num2,dicter[num1][num2]]))
                                res.append([num1,num2,dicter[num1][num2]])
                            
                    elif num2 == dicter[num1][num2]:
                        if count[num2] >= 2:
                            if set([num1,num2,dicter[num1][num2]]) not in setter:
                                setter.append(set([num1,num2,dicter[num1][num2]]))
                                res.append([num1,num2,dicter[num1][num2]])
                    else:
                        if set([num1,num2,dicter[num1][num2]]) not in setter:
                                setter.append(set([num1,num2,dicter[num1][num2]]))
                                res.append([num1,num2,dicter[num1][num2]])

                            
        return res
        

    def find_others(self,nums,index):
        before = nums[:index]
        after = nums[index+1:]
        before.extend(after)
        return before
a = Solution()



print(a.threeSum([0,0,0,0,0]))


def findMin(arr, low, high):
        # This condition is needed to handle the case when array is not
        # rotated at all
    if high < low:
        return arr[0],0

    # If there is only one element left
    if high == low:
        return arr[low],low

    # Find mid
    mid = int((low + high)/2)

    # Check if element (mid+1) is minimum element. Consider
    # the cases like [3, 4, 5, 1, 2]
    if mid < high and arr[mid+1] < arr[mid]:
        return arr[mid+1],mid+1

    # Check if mid itself is minimum element
    if mid > low and arr[mid] < arr[mid - 1]:
        return arr[mid],mid

    # Decide whether we need to go to left half or right half
    if arr[high] > arr[mid]:
        return findMin(arr, low, mid-1)
    return findMin(arr, mid+1, high)
print(findMin([4,5,6,7,-1,0,1,2],0,6))


def letterCombinations(digits):
    dic = {2: "abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
    setter = set([""])

    for i in digits:
        prev = set(setter)
        for j in prev:
            for k in dic[int(i)]:
                res = j + k
                if res not in prev:
                    setter.add(res)
    print setter

def findFirst(arr,x):


        # Check base case
    r = len(arr)-1
    l = 0
    while r >= l:

        mid = (l + r)//2
        # print(mid)


        if arr[mid] == x:
            if mid == 0:
                return mid
            elif findFirst(arr[:mid],x) != -1:

                return min(findFirst(arr[:mid],x),mid)
            return mid
        elif arr[mid] > x:
            r = mid - 1
        elif arr[mid] < x:
            l = mid + 1
        else:
            return -1
    return -1
def findLast(arr,x):

    # Check base case
    r = len(arr)-1
    l = 0
    while r >= l:

        mid = (l + r)//2

        # If element is present at the middle itself
        if arr[mid] == x:
            if findLast(arr[mid+1:],x) != -1:
                return max(mid+1+findLast(arr[mid+1:],x),mid)
            return mid

        elif arr[mid] > x:
            r = mid - 1
        elif arr[mid] < x:
            l = mid + 1
        else:
            return -1
    return -1
# print(findFirst([8,8,8,8],8))
print(findFirst([5,7,7,8,8,10],8))

x = {1:2,3:4}
y = {1:2,3:4,5:6}
print cmp(x, y)

def myPow(x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    if n >= 0:
        if n == 0:
            return 1
        else:
            return myPow(x,n-1)*x
    else:
        if n == 0 :
            return 1
        else:
            return myPow(x,n+1) / float(x)
print(myPow(1.001,12))
def uniquePaths( m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    mat = []
    for i in range(n):
        mat.append([])
        for j in range(m):
            mat[i].append(0)
    # print mat
    for i1 in range(n):
        mat[i][0] = 1
    for j1 in range(m):
        # print m
        mat[0][j] = 1
    for i in range(n):
        for j in range(m):
            mat[i][j] = mat[i-1][j]+mat[i][j-1]
    return mat[n-1][m-1]
print(uniquePaths(3,2))
def setZeroeshelper(matrix,i,j):
    matrix[i] = [0]*len(matrix[i])
    for k in matrix:
        k[j] = 0
    return matrix
print(setZeroeshelper([[1,2],[1,3]],0,1))


def kthSmallest(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    ls =[]
    for i in matrix:
        ls += i
    ls.sort()
    return ls[k-1]
print(kthSmallest([[1,5,9],[10,11,13],[12,13,15]],8))


# print(findLast([5,7,7,8,8,10],8))