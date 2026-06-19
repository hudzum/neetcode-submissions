class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        l, r = 0, 0
        map = defaultdict(int) #store "last seen" index of each number
        res = 1
        
        while r < len(s):
            #is past value less than current
            
            if s[r] in map and map[s[r]]+1 > l :
                #move L to one past value
                l=map[s[r]]+1

                #Update
            map[s[r]] = r
            print(map)
          
            res = max(res, r-l +1)
            r+=1
        return res