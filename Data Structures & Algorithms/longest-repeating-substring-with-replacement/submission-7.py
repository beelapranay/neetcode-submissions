class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i, j, maxLen = 0, 0, 0

        mydict = {}

        while j < len(s):
            mydict[s[j]] = mydict.get(s[j], 0) + 1
            window = j - i + 1
            if (window - max(mydict.values())) <= k:
                maxLen = max(maxLen, window)
            else:
                mydict[s[i]] -= 1
                i += 1
            j += 1
        return maxLen