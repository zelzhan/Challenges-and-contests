class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        res = set()
        for word in words:
            trans = []
            
            for char in word:
                trans.append(morse[ord(char) - ord('a')])
            res.add("".join(trans))
            
        return len(res)
