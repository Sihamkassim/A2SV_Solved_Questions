class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicate=[]
        sortedn=sorted(nums)
        for i in range(len(sortedn)-1):
            if sortedn[i]==sortedn[i+1]:
                duplicate.append(sortedn[i])
            # else:



        return duplicate
        