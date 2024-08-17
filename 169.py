class Solution:
    # Boyer-Moore majority vote algorithm
    def majorityElement(self, nums: list[int]) -> int:
        count = 0

        for num in nums:
            if count == 0:
                majority_element = num
                count = 1
            elif majority_element == num:
                count += 1
            else:
                count -= 1

        return majority_element
