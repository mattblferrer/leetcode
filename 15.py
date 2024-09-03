class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        solutions = set()  # to check for duplicate triplets
        seen_x = set()  # to stop checking duplicate x values early
        indices = dict()
        for i, n in enumerate(nums):  # get maximum index of n in nums
            indices[n] = i

        for i, x in enumerate(nums):  # get value: index pairs in num_dict 
            if x in seen_x:
                continue

            seen_x.add(x)  
            for j, y in enumerate(nums[i + 1:], start=i + 1):
                z = 0 - x - y
                if z not in indices:  # if z has no matching index in nums
                    continue
                if indices[z] <= j:  # if z comes after x and y in nums
                    continue
                st = sorted((x, y, z))  # sorted triple to check duplicates
                solutions.add((st[0], st[1], st[2]))

        return solutions