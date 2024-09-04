class Solution:
    def checkArithmeticSubarrays(self, nums: list[int], l: list[int], r: list[int]) -> list[bool]:
        answer = []
        for l_i, r_i in zip(l, r):
            sequence = sorted(nums[l_i:r_i + 1]) 
            diff = sequence[1] - sequence[0]

            # check differences between adjacent a, b in arithmetic subsequence
            for a, b in zip(sequence, sequence[1:]):  
                if b - a != diff:  # not arithmetic subsequence
                    answer.append(False)
                    break
            else:  # if all differences are the same
                answer.append(True)

        return answer