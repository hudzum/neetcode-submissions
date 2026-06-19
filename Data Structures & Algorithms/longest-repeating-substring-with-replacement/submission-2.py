class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #BF
        res = 0
        for i in range(len(s)):
            maxf=  0
            freq = defaultdict(int)
            for j in range(i, len(s)):
                freq[s[j]] = 1 + freq[s[j]]
                maxf = max(maxf, freq[s[j]])
                winSize = j-i+1 #if j == i it would still be 1 length
                if winSize - maxf <= k:
                    res = max(res, winSize)
        return res