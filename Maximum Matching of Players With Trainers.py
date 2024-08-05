class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        l = 0
        r = 0
        ans = 0
        while l < len(players) and r < len(trainers):
            if players[l] <= trainers[r]:
                ans += 1
                players.pop(l)
                trainers.pop(r)
            else:
                r += 1
        return ans
