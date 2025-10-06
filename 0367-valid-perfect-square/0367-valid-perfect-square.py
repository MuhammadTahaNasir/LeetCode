class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, num
        while l <= r:
            mid = (l + r) // 2
            sq = mid * mid
            if sq == num: return True
            elif sq < num: l = mid + 1
            else: r = mid - 1
        return False