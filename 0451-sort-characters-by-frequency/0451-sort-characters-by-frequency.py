class Solution:
    def frequencySort(self, s: str) -> str:
        counts = {}
        for char in s:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
        
        unique_chars = list(counts.keys())
        
        unique_chars.sort(key=lambda x: counts[x], reverse=True)
        
        result = []
        for char in unique_chars:
            result.append(char * counts[char])
            
        return "".join(result)