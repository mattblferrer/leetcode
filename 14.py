class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        longest_prefix = strs[0]  # list of characters in first word

        # check every word for prefix until non-matching char is found
        for s in strs[1:]:
            if longest_prefix == "":  # if prefix is empty, no need to check
                return longest_prefix

            for i, (char, prefix_char) in enumerate(zip(s, longest_prefix)):
                if char != prefix_char:
                    longest_prefix = longest_prefix[:i]
                    break
            
            # if end of word is reached (all letters in common)
            else:
                if len(s) < len(longest_prefix):
                    longest_prefix = s

        return longest_prefix

