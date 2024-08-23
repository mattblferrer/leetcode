class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        left_ptr, right_ptr = 0, len(nums) - 1
        left_sum, right_sum = 0, 0  # running sum leftSum[i], rightSum[i]
        left_arr, right_arr = [0], [0]  # leftSum, rightSum
        answer = []
        
        while right_ptr > 0:  # iterate through nums from both sides
            left_sum += nums[left_ptr]  # leftSum
            left_arr.append(left_sum)
            left_ptr += 1
            right_sum += nums[right_ptr]  # rightSum
            right_arr.append(right_sum)
            right_ptr -= 1

        for l, r in zip(left_arr, reversed(right_arr)):  # get differences
            answer.append(abs(l - r))

        return answer