import functools, math
from typing import List

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        @functools.lru_cache(None)
        def dp(l: int, r: int, k: int) -> List[int]:
            # l = position of first player (from front)
            # r = position of second player (from end)
            if l == r:
                return [1, 1]  # They face off now
            if l > r:
                return dp(r, l, k)  # normalize ordering

            earliest = math.inf
            latest = -math.inf

            half = (k + 1) // 2
            min_sum = l + r - (k // 2)
            max_sum = half

            for i in range(1, l + 1):
                for j in range(l - i + 1, r - i + 1):
                    s = i + j
                    if not (min_sum <= s <= max_sum):
                        continue
                    nxt = dp(i, j, half)
                    earliest = min(earliest, nxt[0] + 1)
                    latest = max(latest, nxt[1] + 1)

            return [earliest, latest]

        # Convert second player's position from end
        return dp(firstPlayer, n - secondPlayer + 1, n)
