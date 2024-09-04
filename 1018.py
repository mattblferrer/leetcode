class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        prefix_mod = 0
        answer = []
        for n in nums:  # mod 5 at each step for easier calculation
            prefix_mod = (2 * prefix_mod + n) % 5  
            if prefix_mod == 0:  # divisible by 5 (since mod 5)
                answer.append(True)
            else:
                answer.append(False)

        return answer