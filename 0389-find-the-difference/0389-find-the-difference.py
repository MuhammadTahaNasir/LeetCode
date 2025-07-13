class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans = 0
        for c in s + t:
            ans ^= ord(c)
        return chr(ans)