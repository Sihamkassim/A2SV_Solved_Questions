class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window=set()
        left=0
        max_len=0
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[left])
                left +=1
            window.add(s[r])
            max_len = max(max_len,r-left+1)
        return max_len

        