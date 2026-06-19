class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        highestStreak = 0
        for n in nums:
            cur = n
            streak = 0
            while cur in nums:
                streak += 1
                cur += 1
            highestStreak = max(highestStreak, streak)
                
                
        return highestStreak
