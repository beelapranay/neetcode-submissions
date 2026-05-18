class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j, maxa = 0, len(heights) - 1, 0

        while i < j:
            curr = min(heights[i], heights[j]) * (j - i)
            maxa = max(curr, maxa)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        
        return maxa