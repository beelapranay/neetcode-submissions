class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(" ","")
        i = 0
        j = len(s) - 1
        while i < len(s):
            if(s[i] != s[j] and i != j):
                return False
            else:
                i+=1
                j-=1
        return True            

        