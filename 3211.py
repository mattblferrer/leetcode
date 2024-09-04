class Solution:
    def validStrings(self, n: int) -> list[str]:
        if n == 1:
            return ['0', '1']
        strings = []
        for string in self.validStrings(n - 1):
            strings.append(string + '1')  # can add 1 in any case
            if string[-1] == '1':  # only can add another 0 if last char not 0
                strings.append(string + '0') 

        return strings