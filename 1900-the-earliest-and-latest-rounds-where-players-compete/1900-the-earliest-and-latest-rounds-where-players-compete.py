import functools

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> list[int]:
        @functools.lru_cache(None)
        def dp(players: tuple) -> tuple[int, int]:
            k = len(players)
            for i in range(k // 2):
                a, b = players[i], players[-1 - i]
                if {a, b} == {firstPlayer, secondPlayer}:
                    return (1, 1)

            matchups = []
            for i in range(k // 2):
                a, b = players[i], players[-1 - i]
                if firstPlayer in (a, b):
                    winner = firstPlayer
                elif secondPlayer in (a, b):
                    winner = secondPlayer
                else:
                    winner = None
                matchups.append((a, b, winner))

            middle = [players[k // 2]] if k % 2 else []

            res = []
            def dfs(i, next_round):
                if i == len(matchups):
                    nxt = tuple(sorted(next_round + middle))
                    res.append(dp(nxt))
                    return
                a, b, winner = matchups[i]
                if winner:
                    dfs(i + 1, next_round + [winner])
                else:
                    dfs(i + 1, next_round + [a])
                    dfs(i + 1, next_round + [b])

            dfs(0, [])
            min_round = min(x for x, _ in res) + 1
            max_round = max(y for _, y in res) + 1
            return (min_round, max_round)

        # Start with players 1 to n
        return list(dp(tuple(range(1, n + 1))))
