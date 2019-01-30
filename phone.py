
KEYBOARD = {
    '2': ['a','b','c'],
    '3': ['d','e','f'],
    '4': ['g','h','i'],
    '5': ['j','k','l'],
    '6': ['m','n','o'],
    '7': ['p','q','r','s'],
    '8': ['t','u','v'],
    '9': ['w','x','y','z'],
}



"""
Solution with only integers in input digits
"""
class SolutionOnlyInt:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        if not digits:
            return []
            
        results = []
        self.dfs(digits, 0, '', results)
        
        return results
    
    def dfs(self, digits, index, string, results):
        if index == len(digits):
            results.append(string)
            return
        
        for letter in KEYBOARD[digits[index]]:
            self.dfs(digits, index + 1, string + letter, results)







"""
Solution with other letters allowed, not just integers in 
input digits
"""

class SolutionWithLetters:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        if not digits:
            return []
            
        results = []
        self.dfs(digits, 0, '', results)
        
        return results
    
    def dfs(self, digits, index, string, results):
        if index == len(digits):
            results.append(string)
            return
        
        if digits[index] not in KEYBOARD:
            self.dfs(digits, index + 1, string + digits[index], results)
        else:
            for letter in KEYBOARD[digits[index]]:
                self.dfs(digits, index + 1, string + letter, results)





"""
Solution without using trie to implement search in valid word dictionary

Worst case: Everyword generated is in the valid dictionary
(L^K*L) where 
L is the length of characters that map to a single input digit
K is the length of the input digit
N is the number of words in the dictionary

"""

class SolutionWOTrie:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        if not digits:
            return []

        dic = ["dog","hat","map"]
            
        results = []
        self.dfs(digits, 0, '', results)

        ret = []
        dic = set(dic)
        for each in results:
            if each in dic:
                ret.append(each)

        
        return ret
    
    def dfs(self, digits, index, string, results):
        if index == len(digits):
            results.append(string)
            return
        
        if digits[index] not in KEYBOARD:
            self.dfs(digits, index + 1, string + digits[index], results)
        else:
            for letter in KEYBOARD[digits[index]]:
                self.dfs(digits, index + 1, string + letter, results)





"""
Trie 
"""

class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.is_word = False
    
    
class Trie:
    
    def __init__(self):
        self.root = TrieNode()

    """
    @param: word: a word
    @return: nothing
    """
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        
        node.is_word = True

    """
    return the node in the trie if exists 
    """
    def find(self, word):
        node = self.root
        for c in word:
            node = node.children.get(c)
            if node is None:
                return None
        return node
        
    """
    @param: word: A string
    @return: if the word is in the trie.
    """
    def search(self, word):
        node = self.find(word)
        return node is not None and node.is_word

    """
    @param: prefix: A string
    @return: if there is any word in the trie that starts with the given prefix.
    """
    def startsWith(self, prefix):
        return self.find(prefix) is not None


"""
Solution with trie to implement search in valid word dictionary


Worst case: Everyword generated is in the valid dictionary
(L^K*L + NK) where 
L is the length of characters that map to a single input digit
K is the length of the input digit 
N is the number of words in the dictionary

Average case:
O(NK + MK) where 
N is the number of words in the dictionar 
K is the length of each word
M is the number of strings that are generated that are actually in the valid dictionary
"""

class SolutionWithTrie:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        if not digits:
            return []

        dic = ["dog","cat","hat","rat"]
        trie = Trie()
        for each in dic:
            trie.insert(each)

            
        results = []
        self.dfs(digits, 0, '', results,trie)
        
        return results
    
    def dfs(self, digits, index, string, results,trie):
        

        if index == len(digits) and trie.search(string):

            results.append(string)
            return

        if trie.startsWith(string):
            if digits[index] not in KEYBOARD:
                self.dfs(digits, index + 1, string + digits[index], results,trie)
            else:
                for letter in KEYBOARD[digits[index]]:
                    self.dfs(digits, index + 1, string + letter, results,trie)



SolutionWithTrie = SolutionWithTrie()
SolutionWOTrie = SolutionWOTrie()


SolutionOnlyInt = SolutionOnlyInt()

SolutionWithLetters = SolutionWithLetters()




print(SolutionWithTrie.letterCombinations('364'))

print(SolutionWOTrie.letterCombinations('364'))

print(SolutionWOTrie.letterCombinations('364'))

print(SolutionOnlyInt.letterCombinations('2445'))

print(SolutionWithLetters.letterCombinations('24B4KK5'))


