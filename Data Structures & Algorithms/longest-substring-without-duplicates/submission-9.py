class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j, maxLen = 0, 1, 1

        if len(s) < 1:
            return 0

        while j < len(s):
            if s[j] in s[i:j]:
                i += 1
            else:
                maxLen = max(maxLen, j - i + 1)
                j += 1
            
        return maxLen