class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total_length = 0
        
        for word in words:
            
            can_form = True
            for char in word:
                
                if word.count(char) > chars.count(char):
                    can_form = False
                    break
            if can_form:
                total_length += len(word)

        return total_length