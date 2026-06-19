class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word = {}
        if len(t) != len(s):
            return False
        for c in s:
            if c in word.keys():
                word[c] = word[c]+1
            else: 
                word[c] = 1
        print(word)
        for c in t:
            if c in s:
                word[c] -= 1
                if word[c] < 0:
                    return False
                   
            else:
                return False
                
            

        return True
        