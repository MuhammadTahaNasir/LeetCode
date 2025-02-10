class Solution:
    def kthCharacter(self, k: int) -> str:
        def dfs(k):
            if k == 1:
                return 'a'
            # Find largest power of 2 less than or equal to k
            length = 1
            while length * 2 < k:
                length *= 2
            if k <= length:
                return dfs(k)
            else:
                # It's in transformed part, find corresponding character in first half
                ch = dfs(k - length)
                return chr((ord(ch) - ord('a') + 1) % 26 + ord('a'))

        return dfs(k)
