from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt_p=Counter(p)
        len_p=len(p)
        wind_s = Counter(s[:len_p])
        ans=[]
        n=len(p)
        if len(s) < len(p):
            return ans
        if cnt_p == wind_s:
            ans.append(0)
        for i in range(len(p), len(s)):
            wind_s[s[i]] += 1
            wind_s[s[i -n ]] -= 1
            if wind_s[s[i - n]] == 0:
                del wind_s[s[i - n]]
            
            if wind_s == cnt_p:
                ans.append(i - n + 1)
        return ans
