class Solution:
    def matchPlayersAndTrainers(self, players, trainers):
        players.sort()
        trainers.sort()
        
        i = j = matches = 0
        len_p, len_t = len(players), len(trainers)
        
        while i < len_p and j < len_t:
            if players[i] <= trainers[j]:
                matches += 1
                i += 1
            j += 1
            
        return matches
