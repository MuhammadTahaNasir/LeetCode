class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: list[int], endTime: list[int]) -> int:
        n = len(startTime)

        # ✅ Precompute all gaps (fastest access, minimal memory)
        gaps = [startTime[0]]  # Time before first event
        for i in range(1, n):
            gaps.append(startTime[i] - endTime[i - 1])
        gaps.append(eventTime - endTime[-1])  # Time after last event

        # ✅ Use a sliding window of size k+1
        window_sum = sum(gaps[:k + 1])
        max_free = window_sum

        for i in range(k + 1, len(gaps)):
            window_sum += gaps[i] - gaps[i - k - 1]
            max_free = max(max_free, window_sum)

        return max_free
