class Solution:
    def checkDistances(self, s: str, distance: list[int]) -> bool:
        s_distance = [0] * 26  # the true distance between characters in s
        first_occ = dict()  # index of the first occurrence of a letter in s

        for i, letter in enumerate(s):
            if letter not in first_occ:  # first occurrence
                first_occ[letter] = i
            else:  # second occurrence
                position = ord(letter) - 97  # a = 0, b = 1, ...
                s_distance[position] = i - first_occ[letter] - 1

        for i in range(26):  # disregard characters that did not appear in s
            letter = chr(i + 97)  # lowercase ASCII position
            if letter not in first_occ:
                distance[i] = 0

        return s_distance == distance