class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        tokens = s.split(" ")
        last_number = 0

        for token in tokens:
            if not token.isnumeric():  # check if token is not a number
                continue
            if int(token) <= last_number:
                return False
            last_number = int(token)

        return True