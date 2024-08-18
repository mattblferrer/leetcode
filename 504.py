class Solution:
    def convertToBase7(self, num: int) -> str:
        if num < 0:  # if negative, convert -num to base 7 and add sign
            return "-" + self.convertToBase7(-num)
        
        if num == 0:  # zero edge case
            return "0"
        
        # if positive, construct string as loop from smallest
        base_7_str = ""

        while num > 0:
            num, rem = divmod(num, 7)
            base_7_str += str(rem)

        return base_7_str[::-1]  # reverse since ones place is on leftmost
