class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums:
            not_same=0
            for j in nums:
                if i==j:
                    not_same+=1
            if not_same==1:
                return i
        


