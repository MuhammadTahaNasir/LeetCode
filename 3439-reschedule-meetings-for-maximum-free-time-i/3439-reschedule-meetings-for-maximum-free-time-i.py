class Solution:
    def maxFreeTime(self, eventTime: int, k: int, start: list[int], end: list[int]) -> int:
        n = len(start)
        max_free = 0
        window_sum = 0

        # Inline sliding window without extra gap array
        for i in range(n + 1):
            # compute current gap
            if i == 0:
                gap = start[0]
            elif i == n:
                gap = eventTime - end[-1]
            else:
                gap = start[i] - end[i - 1]

            window_sum += gap

            if i > k:
                j = i - k - 1
                if j == 0:
                    old_gap = start[0]
                elif j == n:
                    old_gap = eventTime - end[-1]
                else:
                    old_gap = start[j] - end[j - 1]
                window_sum -= old_gap

            if i >= k:
                max_free = max(max_free, window_sum)

        return max_free
