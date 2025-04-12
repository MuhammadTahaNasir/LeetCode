class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0: return '0'
        n, res = abs(num), []
        while n:
            res.append(str(n % 7))
            n //= 7
        return ('-' if num < 0 else '') + ''.join(reversed(res))