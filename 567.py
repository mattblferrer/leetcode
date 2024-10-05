class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def getFrequency(s: str) -> list[int]:
            frequencies = [0] * 26
            for char in s:
                frequencies[ord(char) - 97] += 1

            return frequencies

        s1_counts = getFrequency(s1)
        s2_counts = getFrequency(s2[:len(s1)])  # substring frequency array
        if s1_counts == s2_counts:  # check if initial substring matches s1
            return True

        for left, right in zip(s2[:len(s2) - len(s1)], s2[len(s1):]):  
            s2_counts[ord(right) - 97] += 1  # add character on right
            s2_counts[ord(left) - 97] -= 1  # remove character on left
            if s1_counts == s2_counts:  # check if substring matches s1
                return True

        return False  # no substring in s2 matched

