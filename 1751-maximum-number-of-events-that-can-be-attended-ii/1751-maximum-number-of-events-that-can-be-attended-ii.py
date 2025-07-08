class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # 1) sort by start‑day
        events.sort()
        n = len(events)

        # 2) pre‑compute the next index that starts after events[i] ends
        starts = [s for s, _, _ in events]                        # just the starts
        next_idx = [bisect_left(starts, events[i][1] + 1)
                    for i in range(n)]                           

        # 3) rolling DP: dp[i] = best value from i..end using (curr remaining‑1) events
        dp = [0] * (n + 1)                                       # for k=0

        for _ in range(k):                                       # <=10 in practice
            new = [0] * (n + 1)
            # go right‑to‑left so we can reuse values already written in `new`
            for i in range(n - 1, -1, -1):
                take = events[i][2] + dp[next_idx[i]]            # attend this + best after it
                skip = new[i + 1]                                # or skip to i+1
                new[i] = take if take > skip else skip
            dp = new                                             # roll forward

        return dp[0]