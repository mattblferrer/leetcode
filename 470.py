# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        random_int = float('inf')
        while random_int > 10:
            random_int = (rand7() - 1) * 7 + rand7() # type: ignore

        return random_int 
        """
        :rtype: int
        """
        