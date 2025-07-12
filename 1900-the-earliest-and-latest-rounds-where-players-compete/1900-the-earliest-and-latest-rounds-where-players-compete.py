from collections import deque

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> list[int]:
        # Ensure firstPlayer < secondPlayer for consistency
        if firstPlayer > secondPlayer:
            firstPlayer, secondPlayer = secondPlayer, firstPlayer

        seen = set()
        q = deque()
        q.append((tuple(range(1, n + 1)), 1))
        earliest = float('inf')
        latest = -float('inf')

        while q:
            players, round_num = q.popleft()
            k = len(players)
            matchups = []
            fp_idx, sp_idx = players.index(firstPlayer), players.index(secondPlayer)

            if fp_idx + sp_idx == k - 1:
                # Players are matched this round
                earliest = min(earliest, round_num)
                latest = max(latest, round_num)
                continue

            for i in range(k // 2):
                matchups.append((players[i], players[-1 - i]))

            middle = (players[k // 2],) if k % 2 else ()

            def simulate(i, winners):
                if i == len(matchups):
                    next_round = tuple(sorted(winners + list(middle)))
                    if next_round not in seen:
                        seen.add(next_round)
                        q.append((next_round, round_num + 1))
                    return
                a, b = matchups[i]
                if {a, b} == {firstPlayer, secondPlayer}:
                    return  # Skip since they're matched and already counted
                elif a == firstPlayer or b == firstPlayer:
                    simulate(i + 1, winners + [firstPlayer])
                elif a == secondPlayer or b == secondPlayer:
                    simulate(i + 1, winners + [secondPlayer])
                else:
                    simulate(i + 1, winners + [a])
                    simulate(i + 1, winners + [b])

            simulate(0, [])

        return [earliest, latest]
