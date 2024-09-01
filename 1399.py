class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = dict()
        for i in range(1, n + 1):  # create groups according to digit sum
            sum_digits = sum(int(d) for d in str(i))
            if sum_digits not in groups:
                groups[sum_digits] = [i]
            else:
                groups[sum_digits].append(i)

        max_size = 0
        max_num = 1  # number of groups with largest size
        for group in groups.values():
            if len(group) > max_size:  # reset maximum
                max_num = 1
                max_size = len(group)
            elif len(group) == max_size:
                max_num += 1

        return max_num