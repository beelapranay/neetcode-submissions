class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mydict = {}
        for i, num in enumerate(numbers):
            res = target - num
            if (res in mydict):
                return [mydict[res] + 1, i+1]
            else:
                mydict[num] = i
        return None            
