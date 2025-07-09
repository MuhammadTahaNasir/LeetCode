class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: list[int], endTime: list[int]) -> int:
        n = len(startTime)

        # Precompute gaps array (faster than computing inside loop)
        gaps = [0] * (n + 1)
        gaps[0] = startTime[0]  # Before first event

        for i in range(1, n):
            gaps[i] = startTime[i] - endTime[i - 1]  # Between events

        gaps[n] = eventTime - endTime[-1]  # After last event

        # Sliding window
        window_sum = sum(gaps[:k + 1])
        max_free = window_sum

        for i in range(k + 1, len(gaps)):
            window_sum += gaps[i] - gaps[i - k - 1]
            max_free = max(max_free, window_sum)

        return max_free
