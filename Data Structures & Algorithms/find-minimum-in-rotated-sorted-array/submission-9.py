class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums)-1

        res = float("inf")

        while l <= r:
            mid = (l+r) // 2 

            #section is increasing
            if nums[l] < nums[mid]:
                res = min(res, nums[l])



            mid = (l+r) // 2 # floor 
            res = min(res, nums[mid]) #incase mid is min

            #first is Ascending
            if nums[l] <= nums[mid]:
                #move to other section
                l = mid+1
            #first is not scending
            else:
                r = mid -1

        return res


            
