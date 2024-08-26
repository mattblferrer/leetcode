class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        if a > b:
            a, b = b, a  # swap so a is the smaller element
        # calculate number of factors in a that is common with b
        common_factors = 0 
        for i in range(1, a + 1):
            if a % i == 0 and b % i == 0:
                common_factors += 1

        return common_factors