class Solution:
    def bestHand(self, ranks: list[int], suits: list[str]) -> str:
        def isFlush(suits: list[str]) -> bool:
            return len(set(suits)) == 1

        def isThreeOfAKind(ranks: list[int]) -> bool:
            rank_count = [0] * 14
            for rank in ranks:
                rank_count[rank] += 1
            return max(rank_count) >= 3
        
        def isPair(ranks: list[int]) -> bool:
            rank_count = [0] * 14
            for rank in ranks:
                rank_count[rank] += 1
            return max(rank_count) == 2

        # identify poker hand based on ranks and suits
        if isFlush(suits):
            return "Flush"
        if isThreeOfAKind(ranks):
            return "Three of a Kind"
        if isPair(ranks):
            return "Pair"
        return "High Card"