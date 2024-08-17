class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = dict()  # stores index of char in substring
        maximum_length = 0
        current_length = 0
        string_length = len(s)
        start_ptr = 0  # starting pointer index of s
        curr_ptr = 0  # current pointer index of s

        # loop through substrings until the end of s
        while curr_ptr < string_length:
            char = s[curr_ptr]

            # if repeated char found, slide start_ptr to the right
            if char in seen and seen[char] >= start_ptr:
                current_length -= seen[char] - start_ptr + 1
                start_ptr = seen[char] + 1

            # slide curr_ptr to the right
            seen[char] = curr_ptr
            curr_ptr += 1
            current_length += 1

            if maximum_length < current_length:  # update length
                maximum_length = current_length
                
        return maximum_length
    