class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalprod = 1
        result = [0] * len(nums)
        zerocnt = 0
        zeroindex= len(nums)+1
        for i, n in enumerate(nums):
            
            
            if n == 0:
                zeroindex = i
                zerocnt +=1
            else:
                totalprod *=n 

        if zerocnt > 1:
            return [0] * len(nums)
        for i, n in enumerate(nums):
            if zerocnt:
                result[i] = 0 if n else totalprod
            else:
                result[i] = totalprod // n
            

        return result
            