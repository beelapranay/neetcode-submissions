class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        myset = set(nums)

        for i in myset:
            if (i-1) not in myset:
                count = 1
                current = i
                while (current + 1) in myset:
                    count += 1
                    current += 1
                longest = max(count, longest)
        return longest        
        