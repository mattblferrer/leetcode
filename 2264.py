class Solution:
    def largestGoodInteger(self, num: str) -> str:
        good_integers = set()  # stores one digit of good integers found
        for i in range(len(num) - 2):
            substring = num[i:i + 3]
            if substring[0] == substring[1] == substring[2]:
                good_integers.add(int(substring[0]))  # since all same digit

        if good_integers:  # check if any good integers found
            return str(max(good_integers)) * 3
        return ""