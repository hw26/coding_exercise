

"""
Alien Dictionary

Worst case:
O(N^2) where N is total number of characters in the dictionary
potentially every character has an edge to every other character

Average case:
O(N) where N is total number of characters in the dictionary

"""

class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        import heapq
        


        graph = {}
        
        for i in range(len(words)) :
            for j in range(len(words[i])) :
                c = words[i][j]
                graph[c] = set()
          
        
        for i in range(len(words)-1) :
            index = 0
            while index < len(words[i]) and (index < len(words[i + 1])):
                if (words[i][index] != words[i + 1][index]) :
                    graph[words[i][index]].add(words[i + 1][index])
                    break
                
                index+= 1

        
        indegree = {}
        for u in graph:
            indegree[u] = 0
        
        
        for  u in graph:
            for v in graph[u] :
                indegree[v] += 1

        q = []
        
        for u in indegree:
            if (indegree[u] == 0) :
                heapq.heappush(q , u)
            
        order = ""
        while q:
            head = heapq.heappop(q)
            order += head
            for neighbor in graph[head]:
                indegree[neighbor]  -= 1
                if (indegree[neighbor] == 0) :
                    heapq.heappush(q , neighbor)
        
        if len(order) != len(graph):
            return ""
        
        return order