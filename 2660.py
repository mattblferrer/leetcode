class Solution:
    def isWinner(self, player1: list[int], player2: list[int]) -> int:
        score1, score2 = 0, 0
        for i, (s1, s2) in enumerate(zip(player1, player2)):
            if i == 0:  # no previous turns yet
                score1 += s1
                score2 += s2
                continue
            if player1[i - 1] == 10 or player1[max(i - 2, 0)] == 10:
                score1 += s1 * 2
            else:
                score1 += s1
            if player2[i - 1] == 10 or player2[max(i - 2, 0)] == 10:
                score2 += s2 * 2
            else:
                score2 += s2
                
        if score1 > score2:  # player 1 win
            return 1
        elif score2 > score1:  # player 2 win
            return 2
        return 0  # draw