class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        for i in range(min(len1, len2), 0, -1):  # start with largest substring
            if len1 % i != 0 or len2 % i != 0:
                continue
            substr1 = str1[:i]
            substr2 = str2[:i]
            if substr1 * (len1 // i) != str1:  # check if substr1 repeats
                continue
            if substr2 * (len2 // i) != str2:  # check if substr2 repeats
                continue
            if substr1 != substr2:
                continue
            return substr1  # if all conditions passed

        return ""  # if no gcd substring found