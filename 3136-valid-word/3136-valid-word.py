class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        has_vowel = False
        has_consonant = False

        for ch in word:
            if not ch.isalnum():
                return False
            if ch.isalpha():
                c = ch.lower()
                if c in 'aeiou':
                    has_vowel = True
                else:
                    has_consonant = True

        return has_vowel and has_consonant
