class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mydict = {}
        j = 0

        while j < len(s1):
            mydict[s1[j]] = mydict.get(s1[j], 0) + 1
            j += 1

        i, j = 0, len(s1) - 1

        while j < len(s2):
            while i <= j:
                if s2[i] in mydict:
                    mydict[s2[i]] -= 1
                i += 1

            if max(mydict.values()) == 0:
                return True

            i += 1
            j += 1
        
        return False
