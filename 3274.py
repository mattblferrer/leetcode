class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        def colorChessboard(file: str, rank: int) -> bool:  # black 0, white 1
            if file in 'aceg':
                return rank % 2 == 1
            else:
                return rank % 2 == 0

        file1, rank1 = coordinate1[0], int(coordinate1[1])
        file2, rank2 = coordinate2[0], int(coordinate2[1])
        return colorChessboard(file1, rank1) == colorChessboard(file2, rank2)