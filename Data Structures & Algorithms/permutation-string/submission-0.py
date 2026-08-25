class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        j = 0
        mydict = {}

        while j < len(s1):
            mydict[s1[j]] = mydict.get(s1[j], 0) + 1
            j += 1

        j = 0

        while j < len(s2):
            if (s2[j] in mydict):
                mydict[s2[j]] -= 1
            j += 1

        if (max(mydict.values()) == 0):
            return True
        else:
            return False                