from collections import defaultdict
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if not ransomNote:
            return True
        hashtable = defaultdict(int)
        for char in ransomNote:
            hashtable[char]+=1
        
        for value in magazine:
            if hashtable[value] > 0:
                hashtable[value]-=1
            if hashtable[value] == 0:
                del hashtable[value]
                if not hashtable.values():
                    return True
        return False
