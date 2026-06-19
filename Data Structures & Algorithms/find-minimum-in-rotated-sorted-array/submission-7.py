class Solution:
    def findMin(self, nums: List[int]) -> int:
        #Find Unsorted Section
        l = 0
        r = len(nums)-1
        res = float("inf")
        while l <= r:
            #section isnt rotated
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            print(res)
            mid = (l+r)//2
            res = min(res, nums[mid])
            #l -> mid sorted
            #right side sorted
            if nums[mid] < nums[r]:
                r= mid -1
            #if left side sorted
            else:
                l = mid +1
            print(res)
        return res
            
