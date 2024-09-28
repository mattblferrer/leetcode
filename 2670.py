class Solution:
    def distinctDifferenceArray(self, nums: list[int]) -> list[int]:
        prefix_dict = {}  # Counter of prefix nums[0, ..., i]
        suffix_dict = {}  # Counter of suffix nums[i + 1, ..., n + 1]
        diff = []

        for n in nums:  # get frequencies of nums as initial suffix dictionary
            if n not in suffix_dict:
                suffix_dict[n] = 1
            else:
                suffix_dict[n] += 1

        for n in nums:
            if n not in prefix_dict:  # add to prefix dictionary
                prefix_dict[n] = 1
            else:
                prefix_dict[n] += 1

            if n in suffix_dict:  # remove from suffix dictionary
                suffix_dict[n] -= 1
                if suffix_dict[n] == 0:  # if last occurrence of n, delete
                    del suffix_dict[n]

            diff.append(len(prefix_dict) - len(suffix_dict))

        return diff