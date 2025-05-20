from typing import List

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players = sorted(players)
        trainers = sorted(trainers)

        i = j = 0

        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                i += 1
            j += 1
        return i