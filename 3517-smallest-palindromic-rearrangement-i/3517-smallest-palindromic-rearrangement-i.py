from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = Counter(s)

        half = []
        middle = ""

        for ch in sorted(freq.keys()):
            count = freq[ch]
            print(freq)
            
            half.append(ch * (count // 2))
            if count % 2 == 1:
                middle = ch

        half = "".join(half)

        return half + middle + half[::-1]