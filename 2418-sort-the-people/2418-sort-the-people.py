class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        nums_h=list(zip(names,heights))
        n = len(names)
        
        min_index = 0
        for i in range(n):
            for j in range(n-1):
                if nums_h[i][-1] > nums_h[j][-1]:
                    nums_h[i] , nums_h[j] = nums_h[j] , nums_h[i]
            min_index += 1
        return [name for name , height in nums_h]

        
        