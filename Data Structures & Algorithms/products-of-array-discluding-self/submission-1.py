class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i, n in enumerate(nums):
            totalprod = 1
            for iy, y in enumerate(nums):
                if iy !=i:
                    totalprod *= y

            result.append(totalprod)
        return result