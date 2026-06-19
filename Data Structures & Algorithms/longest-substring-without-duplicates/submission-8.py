class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
    
        #Set for duplicate checking
        #for loop check if in set if 
        #Not gonna work for dvdf because on clear it removes whole set4
    
        l, r = 0, 0
        cur = set()
        longest = 1
        while r < len(s):
            if s[r] not in cur:
                cur.add(s[r])
                print(cur)
                longest = max(longest, len(cur))
            else:
                #stupid idiot
                while s[r] != s[l]:
                    cur.discard(s[l])
                    l+=1
                l+=1 #get rid of left duplicate
                cur.add(s[r])
            r+=1
        return longest