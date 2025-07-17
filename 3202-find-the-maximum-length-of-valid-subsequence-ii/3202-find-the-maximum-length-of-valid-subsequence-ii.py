class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        # dp[x][y] = length of longest valid subsequence where:
        # last element % k == x, second-to-last % k == y
        dp = [[0] * k for _ in range(k)]
        ans = 0

        for num in nums:
            x = num % k
            for j in range(k):
                y = (j - x + k) % k
                dp[x][y] = dp[y][x] + 1
                ans = max(ans, dp[x][y])

        return ans