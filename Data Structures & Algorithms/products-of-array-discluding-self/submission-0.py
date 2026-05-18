class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zc, prod = 0, 1

        for j in nums:
            if j == 0:
                zc += 1
            else:
                prod *= j
        
        j = 0
        
        for j in range(len(nums)):
            if zc > 1:
                nums[j] = 0
            elif zc == 1:
                nums[j] = prod if nums[j] == 0 else 0
            else:
                nums[j] = prod // nums[j]
        
        return nums