class Solution:
    def matchPlayersAndTrainers(self, players, trainers):
        players.sort()
        trainers.sort()
        players = deque(players)
        trainers = deque(trainers)
        matches = 0

        while players and trainers:
            if players[0] <= trainers[0]:
                players.popleft()
                trainers.popleft()
                matches += 1
            else:
                trainers.popleft()  # Trainer too weak
        return matches