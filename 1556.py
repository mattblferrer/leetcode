class Solution:
    def thousandSeparator(self, n: int) -> str:
        # split into groups of 3 digits from right
        groups = []
        count = 0
        group = ""
        for c in reversed(str(n)):  # iterate from right
            group += c
            count += 1
            if count == 3:  # reset for new digit group
                groups.append(group[::-1])  # reverse since right to left
                group = ""
                count = 0

        if group:  # if leftmost digit group exists (length % 3 != 0)
            groups.append(group[::-1])

        # add string converted groups of digits to final result
        result = ""
        for group in reversed(groups):
            result += group + "."

        return result[:-1]  # remove trailing .