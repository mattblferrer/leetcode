class Solution:
    def getGoodIndices(self, variables: list[list[int]], target: int) -> list[int]:
        good_indices = []
        for i, (a, b, c, m) in enumerate(variables):
            if (pow(pow(a, b, 10), c, m)) == target:  # check modular exp
                good_indices.append(i)

        return good_indices