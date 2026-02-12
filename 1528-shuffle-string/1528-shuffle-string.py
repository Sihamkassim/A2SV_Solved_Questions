class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans=[""]*len(s)
    
        for idx , i in enumerate(s):
            target_index=indices[idx]
            ans[target_index] = i
        return "".join(ans)





        