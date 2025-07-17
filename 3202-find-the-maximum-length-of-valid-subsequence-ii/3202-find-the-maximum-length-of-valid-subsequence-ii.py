class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        # dp[i][j] = length of longest valid subsequence
        # ending with last % k == i and expecting next such that (prev + next) % k == j
        dp = [[0] * k for _ in range(k)]
        ans = 0

        for x in nums:
            r = x % k
            for j in range(k):
                dp[r][j] = dp[j][r] + 1
                ans = max(ans, dp[r][j])

        return ans
