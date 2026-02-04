class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for strng in strs[1:]:
            while not strng.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix