class Solution:
    def isValid(self, word: str) -> bool:
        n = len(word)
        if n < 3:
            return False

        hv = False  # vowel found
        hc = False  # consonant found

        for ch in word:
            oc = ord(ch)
            # digits?
            if 48 <= oc <= 57:
                continue
            # uppercase letters?
            if 65 <= oc <= 90:
                offset = oc
                is_v = ((offset * (offset - 65) * (offset - 69)
                         * (offset - 73) * (offset - 79) * (offset - 85)) == 0)
                if is_v:
                    hv = True
                else:
                    hc = True
                continue
            # lowercase letters?
            if 97 <= oc <= 122:
                offset = oc
                is_v = ((offset * (offset - 97) * (offset - 101)
                         * (offset - 105) * (offset - 111) * (offset - 117)) == 0)
                if is_v:
                    hv = True
                else:
                    hc = True
                continue

            # invalid character
            return False

        return hv and hc
