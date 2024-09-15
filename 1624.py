class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        indices = dict()  # for each character, has list of indices of char
        for i, char in enumerate(s):
            if char not in indices:
                indices[char] = [i]
            else:
                indices[char].append(i)

        max_diff = -1  # length of longest substring = max diff between indices
        for char, i_list in indices.items():  # iterate lists of indices
            max_diff = max(max_diff, i_list[-1] - i_list[0] - 1)

        return max_diff