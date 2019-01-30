

"""-------------------------------------------Fibonacci-------------------------------------------"""

"""
sliding window
"""
class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """
    def fibonacci(self, n):
        # write your code here
        dp = [0,1]
        for ii in range(1,n+1):
            dp[ii%2] = dp[(ii-1)%2] + dp[(ii-2)%2]
        return dp[(n-1)%2]

class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """
    def fibonacci(self, n):
        # write your code here
        # dp = [0,1]
        dp = [0 for _ in range(n+1)]
        dp[1] = 1
        for ii in range(1,n+1):
            dp[ii] = dp[(ii-1)] + dp[(ii-2)]
        return dp[n-1]


class Solution:
    def fibonacci(self, n):
        a = 0
        b = 1
        for i in range(n - 1):
            a, b = b, a + b
        return a


"""Recursion"""

class Solution:
    def fibonacci(self, n):
        if n == 1:
            return 0
        if n == 2:
            return 1
        return self.fibonacci(n-2) + self.fibonacci(n-1)
a = Solution()

"""-------------------------------------------Cards-------------------------------------------"""


import random

SUITS = ('Club', 'Spade', 'Heart', 'Diamond')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
    def __str__(self,):
        return (self.suit + " " + self.rank)
        
        
# define hand class

        
# define deck class 
class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()
d = Deck()
d.shuffle()
print(d.deal_card())
d.shuffle()
print(d.deal_card())
print(d.deal_card())
print(len(d.cards))






class Solution:
    """
    @param n: an integer
    @return: return a string
    """
    def lastFourDigitsOfFn(self, n):
        if n == 0 or n == 1:
            return self.format_result(n)
        base_matrix = [[1, 1], [1, 0]]
        result = self.get_n_matrix(n, base_matrix)
        return self.format_result(result)
    
    """ print in format """
    def format_result(self, n):
        if n == 0:
            return '0'
        else:
            n = str(n)
            if len(n) < 4:
                added_zeros = 4 - len(n)
                for i in range(added_zeros):
                    n = '0' + n
            return n
    
    """ fast power """
    def get_n_matrix(self, n, base_matrix):
        n = n - 1
        result = [[1, 0], [0, 1]] 
        product = base_matrix
        while n != 0:
            if n != n >> 1 << 1:
                result = self.get_2x2_matrix_product(result, product)
            n = n >> 1
            product = self.get_2x2_matrix_product(product, product)
        return result[0][0]

    """ matrix mult """
    def get_2x2_matrix_product(self, m1, m2):
        result = [[0 for j in range(2)] for i in range(2)]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    result[i][j] += m1[i][k] * m2[k][j] 
                    result[i][j] = result[i][j] % 10000
        return result

    
    