class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mydict = {}

        i, j, maxLen = 0, 1, 1
        
        while j < len(s):
            mydict[s[j]] = mydict.get(s[j], 0) + 1
            window = j - i + 1

            if window - max(mydict.values()) <= k:
                maxLen = max(window, maxLen)
                j += 1
            else:
                i += 1
        
        return maxLen