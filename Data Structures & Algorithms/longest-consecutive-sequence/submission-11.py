class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = sorted(nums)
        print(n)
        i = 0
        highstr = 0
        cur = n[0]
        streak = 0
        while i < len(n):
            if cur != n[i]: 
                cur = n[i]
                streak = 0
            while i < len(n) and n[i] ==cur:
                i+=1
            streak +=1
            cur += 1
            highstr= max(highstr, streak) 

        return highstr    
