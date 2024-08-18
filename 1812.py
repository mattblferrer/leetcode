class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        if coordinates[0] in ['a', 'c', 'e', 'g']:  # check file
            if int(coordinates[1]) % 2 == 0:  # if even rank, white
                return True
            return False  # if odd rank, black

        if int(coordinates[1]) % 2 == 0:  # if even rank, black
            return False
        return True  # if odd rank, white