class Solution:
    def maxFreeTime(self, eventTime: int, startTime: list[int], endTime: list[int]) -> int:
        n = len(startTime)

        # Step 1: Calculate the free time gaps between meetings
        gaps = [startTime[0]]  # Free time before first meeting
        for i in range(1, n):
            gaps.append(startTime[i] - endTime[i - 1])
        gaps.append(eventTime - endTime[-1])  # Free time after last meeting

        # Step 2: Find maximum prefix and suffix gaps on-the-fly
        prefixMax = [0] * (n + 1)
        suffixMax = [0] * (n + 1)
        prefixMax[0] = gaps[0]
        for i in range(1, n + 1):
            prefixMax[i] = max(prefixMax[i - 1], gaps[i])
        suffixMax[n] = gaps[n]
        for i in range(n - 1, -1, -1):
            suffixMax[i] = max(suffixMax[i + 1], gaps[i])

        # Step 3: Try rescheduling each meeting to combine two adjacent gaps
        maxFree = 0
        for i in range(n):
            meetingDuration = endTime[i] - startTime[i]
            mergedGap = gaps[i] + gaps[i + 1]

            # Max available single gap to place this meeting (excluding current one)
            maxOtherGap = max(
                prefixMax[i - 1] if i > 0 else 0,
                suffixMax[i + 2] if i + 2 <= n else 0
            )

            # Can we move the meeting to a larger gap elsewhere?
            if meetingDuration <= maxOtherGap:
                maxFree = max(maxFree, mergedGap + meetingDuration)
            else:
                maxFree = max(maxFree, mergedGap)

        return maxFree
