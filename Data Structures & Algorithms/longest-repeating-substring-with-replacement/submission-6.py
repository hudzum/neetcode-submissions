class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Slid window
        #instead of every check every substring we fix target character c 
            #how long can window be c if using at most k replacements
        l = 0
        r = 0
        res = 0
        freq = defaultdict(int)
        maxf = 0
        while r < len(s):
            freq[s[r]] += 1
            maxf = max(maxf,freq[s[r]])

            while (r-l+1) - maxf > k:
                freq[s[l]]-=1
                l+=1
            res = max(res, r-l+1)


            r+=1
        return res
            
            