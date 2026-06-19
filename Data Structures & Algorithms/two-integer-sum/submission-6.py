class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Brute Force we can create a double for loop 
        freq = {}
        for n in range(len(nums)):
            if freq.get(target-nums[n]) != None:
                return [freq[target-nums[n]], n]
            else:
                freq[nums[n]] = n
        
