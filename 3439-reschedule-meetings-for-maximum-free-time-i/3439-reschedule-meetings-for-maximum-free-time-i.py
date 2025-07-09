class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: list[int], endTime: list[int]) -> int:
        n = len(startTime)
        max_free = 0
        window_sum = 0

        # Process each gap on the fly without storing them
        for i in range(n + 1):
            # Compute current gap
            if i == 0:
                gap = startTime[0]
            elif i == n:
                gap = eventTime - endTime[-1]
            else:
                gap = startTime[i] - endTime[i - 1]

            window_sum += gap

            # Remove oldest gap when window exceeds size k+1
            if i > k:
                if i - k - 1 == 0:
                    old_gap = startTime[0]
                elif i - k - 1 == n:
                    old_gap = eventTime - endTime[-1]
                else:
                    old_gap = startTime[i - k - 1] - endTime[i - k - 2]
                window_sum -= old_gap

            if i >= k:
                max_free = max(max_free, window_sum)

        return max_free
