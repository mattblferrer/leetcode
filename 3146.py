class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        s_indices, t_indices = [-1] * 26, [-1] * 26

        # get letter indices of each letter in s and t
        for i, (s_letter, t_letter) in enumerate(zip(s, t)):
            s_pos, t_pos = ord(s_letter) - 97, ord(t_letter) - 97
            s_indices[s_pos] = i
            t_indices[t_pos] = i

        # get permutation difference between s and t
        difference = 0
        for (s_i, t_i) in zip(s_indices, t_indices):
            difference += abs(s_i - t_i)

        return difference 
