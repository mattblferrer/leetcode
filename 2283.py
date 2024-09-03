class Solution:
    def digitCount(self, num: str) -> bool:
        counts = dict()
        for digit in num:  # get digit counts for each digit value
            if int(digit) not in counts:
                counts[int(digit)] = 1
            else:
                counts[int(digit)] += 1

        for i, digit in enumerate(num):  
            if i not in counts:
                if int(digit) != 0:
                    return False
            elif int(digit) != counts[i]:  # check digit count == digit value
                return False
        return True