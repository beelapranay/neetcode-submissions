class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j, maxlen = 0, 1, 0

        while j < len(s):
            if s[j] in s[i : j]:
                i += 1
            else:
                maxlen = max(maxlen, j - i + 1)
            j += 1
        
        return maxlen