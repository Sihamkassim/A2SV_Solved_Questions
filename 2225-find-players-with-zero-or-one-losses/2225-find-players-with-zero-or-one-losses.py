from collections import Counter
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        looser=[]
        winner=[]
        for y in matches:
            winner.append(y[0])
            looser.append(y[1])
        cnt=Counter(looser)
        Ultimate_winner=[players for players in set(winner) if players not in cnt]
        Slightly_winner=[player for player in cnt if cnt[player]==1]
        return [sorted(Ultimate_winner), sorted(Slightly_winner)]