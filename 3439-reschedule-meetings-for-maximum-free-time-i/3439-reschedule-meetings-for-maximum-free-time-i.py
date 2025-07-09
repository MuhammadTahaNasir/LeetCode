class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: list[int], endTime: list[int]) -> int:
        n = len(startTime)
        # Precompute all gaps to eliminate any runtime computation inside hot loop
        gaps = [startTime[0]]  # Before the first event
        gaps += [startTime[i] - endTime[i - 1] for i in range(1, n)]  # Between events
        gaps.append(eventTime - endTime[-1])  # After the last event

        max_free = window_sum = sum(gaps[:k + 1])
        for i in range(k + 1, len(gaps)):
            window_sum += gaps[i] - gaps[i - k - 1]
            max_free = max(max_free, window_sum)

        return max_free