class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        has_vowel = False
        has_consonant = False

        for ch in word:
            # Only letters and digits allowed
            if not ('0' <= ch <= '9' or 'A' <= ch <= 'Z' or 'a' <= ch <= 'z'):
                return False

            # Check only if it's a letter
            if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
                # Convert uppercase vowels manually (no .lower or in lookup)
                if ch in 'AEIOUaeiou':
                    has_vowel = True
                else:
                    has_consonant = True

        return has_vowel and has_consonant
