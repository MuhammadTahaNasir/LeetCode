class Solution:
    def possibleStringCount(self, word: str) -> int:
        n = len(word)
        i = 0
        total = 0  # Count of possible original strings

        while i < n:
            j = i
            # Find the end of current group of same chars
            while j < n and word[j] == word[i]:
                j += 1
            group_length = j - i
            if group_length >= 2:
                total += group_length - 1  # How many shorter versions we can make
            i = j
        
        return total + 1  # +1 for the original unreduced word
