class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        min_index_row = []  
        for row in matrix:  
            minimum = float('inf')
            for i, n in enumerate(row):  # find minimum in row
                if n < minimum:
                    minimum = n
                    min_index = i
                    
            min_index_row.append((min_index, minimum))

        lucky = []
        for i, min_row in min_index_row:  # check for lucky numbers
            for row_check in matrix:  # check if maximum in column
                if row_check[i] > min_row:
                    break
            else:  # if no greater element appears in column
                lucky.append(min_row)

        return lucky