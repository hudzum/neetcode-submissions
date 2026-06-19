class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
    
        #Set for duplicate checking
        #for loop check if in set if 
        #Not gonna work for dvdf because on clear it removes whole set4
    
        l, r = 0, 0
        cur = set()
        res = 1
        while r < len(s):
            #Add Elements to sets
            #if duplicate
            #move through 
            while s[r] in cur:
                cur.discard(s[l])
                l+=1
            cur.add(s[r])
            r+=1
            res = max(res, r-l)

        return res