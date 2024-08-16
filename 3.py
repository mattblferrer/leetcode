class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        maximum_length = 0
        current_length = 0
        start_ptr = 0  # starting pointer index of s
        curr_ptr = 0  # current pointer index of s

        # loop through substrings until the end of s
        while curr_ptr != len(s):
            # if repeated char found, reset pointers and seen set
            if s[curr_ptr] in seen:
                current_length = 0
                seen = set()
                start_ptr += 1
                curr_ptr = start_ptr

            # if repeated char not yet found
            else:
                seen.add(s[curr_ptr])
                current_length += 1  
                curr_ptr += 1

                if maximum_length < current_length:  # update length
                    maximum_length = current_length
                
        return maximum_length