from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        graph = defaultdict(set)
        
        wordList.append(beginWord)
        
        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + '*' + word[i+1:] 
                graph[key].add(word)
                graph[word].add(key)
                
        
        queue = [(beginWord, 0)]
        
        visited = {beginWord}
        
        while queue:
            
            node, level = queue.pop(0)
            
            if node == endWord:
                return level + 1
            
            for inter in graph[node]:
                for adj in graph[inter]:
                    if adj not in visited:
                        visited.add(adj)
                        queue.append((adj, level+1))
          
        
        return 0
        
        
        
        
        
        
