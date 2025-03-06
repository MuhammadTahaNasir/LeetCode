class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        ans = 0
        j = 0  # Pointer for trainers

        for player in players:
            while j < len(trainers) and trainers[j] < player:
                j += 1
            if j < len(trainers):
                ans += 1
                j += 1

        return ans
