class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j, maxLen = 0, 0, 0

        while j < len(s):
            while s[j] in s[i : j]:
                i += 1
            maxLen = max(maxLen, j - i + 1)
            j += 1
        return maxLen            