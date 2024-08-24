class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        arr = [first]
        decoded = first
        for num in encoded:  # xor to reverse encoded xor operation
            decoded ^= num
            arr.append(decoded)

        return arr