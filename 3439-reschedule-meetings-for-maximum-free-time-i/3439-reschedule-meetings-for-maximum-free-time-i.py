class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: list[int], endTime: list[int]) -> int:
        n = len(startTime)
        max_free = 0
        window_sum = 0

        for i in range(n + 1):
            # Efficient gap calculation with minimal branching
            if i == 0:
                gap = startTime[0]
            elif i == n:
                gap = eventTime - endTime[n - 1]
            else:
                gap = startTime[i] - endTime[i - 1]

            window_sum += gap

            if i > k:
                j = i - k - 1
                if j == 0:
                    window_sum -= startTime[0]
                elif j == n:
                    window_sum -= eventTime - endTime[n - 1]
                else:
                    window_sum -= startTime[j] - endTime[j - 1]

            if i >= k:
                max_free = max(max_free, window_sum)

        return max_free