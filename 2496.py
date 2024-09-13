class Solution:
    def maximumValue(self, strs: list[str]) -> int:
        max_value = 0
        for string in strs:
            if string.isnumeric():
                max_value = max(max_value, int(string))
            else:
                max_value = max(max_value, len(string))
        
        return max_value  