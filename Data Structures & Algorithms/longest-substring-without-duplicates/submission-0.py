class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 1:
            return 0

        i, maxLength = 0, 1

        for j in range(1, len(s)):
            while s[j] in s[i:j]:
                i+=1
            maxLength = max(maxLength, j - i + 1)
        return maxLength        

