class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_num = 0
        for stone in stones:
            if stone in jewels:
                jewels_num += 1

        return jewels_num