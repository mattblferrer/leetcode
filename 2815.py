class Solution:
    def maxSum(self, nums: list[int]) -> int:
        max_digit_dict = {}

        for n in nums:  # populate dictionary with max_digit: [nums] pairs
            max_digit = max(int(digit) for digit in str(n)) 
            if max_digit not in max_digit_dict:  # initialize array
                max_digit_dict[max_digit] = [n]
            else:  # new number with same max digit found
                max_digit_dict[max_digit].append(n)

        max_pair_sum = -1
        for k, v in max_digit_dict.items():
            if len(v) == 1:  # no pair can be found
                continue
                
            max_digit_nums = sorted(max_digit_dict[k])
            curr_pair_sum = max_digit_nums[-2] + max_digit_nums[-1]
            max_pair_sum = max(max_pair_sum, curr_pair_sum)
        
        return max_pair_sum