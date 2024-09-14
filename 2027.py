class Solution:
    def minimumMoves(self, s: str) -> int:
        indices = [i for i, char in enumerate(s) if char == 'X']
        moves = 0
        ptr = 0  # pointer to iterate through indices with X 

        while ptr < len(indices):
            next_indices = indices[ptr + 1:ptr + 3]  # next 2 indices with X
            left = indices[ptr]  # leftmost index of 3 consecutive
            for x in next_indices:  
                if x - left < 3:  # if next indices within 3 consecutive
                    ptr += 1  # convert to O

            ptr += 1  # convert to O
            moves += 1

        return moves