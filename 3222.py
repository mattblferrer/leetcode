class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        turn = 0  # if 0, Alice's turn, if 1, Bob's turn
        while True:
            x -= 1
            y -= 4
            turn = 1 - turn  # pass turn to other player

            if x < 0 or y < 0:
                if turn:
                    return "Bob"
                return "Alice"