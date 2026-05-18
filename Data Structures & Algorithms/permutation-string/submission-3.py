class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts_s1 = [0] * 26
        counts_s2 = [0] * 26

        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False

        for i in range(n1):
            counts_s1[ord(s1[i]) - ord('a')] += 1
            counts_s2[ord(s2[i]) - ord('a')] += 1
        
        if counts_s1 == counts_s2:
            return True
        
        for i in range(n1, n2):
            counts_s2[ord(s2[i]) - ord('a')] += 1
            counts_s2[ord(s2[i - n1]) - ord('a')] -= 1
            if counts_s1 == counts_s2:
                return True
        
        return False