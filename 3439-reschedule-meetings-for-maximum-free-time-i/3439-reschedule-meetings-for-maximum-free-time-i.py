
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)

        # Step 1: Calculate all gaps (before first, between, after last)
        gaps = [startTime[0]]  # Time before the first event
        for i in range(1, n):
            gaps.append(startTime[i] - endTime[i - 1])  # Time between events
        gaps.append(eventTime - endTime[-1])  # Time after the last event

        # Step 2: Use sliding window of size k + 1
        window_sum = sum(gaps[:k + 1])
        max_free = window_sum

        for i in range(k + 1, len(gaps)):
            window_sum += gaps[i] - gaps[i - k - 1]
            max_free = max(max_free, window_sum)

        return max_free
