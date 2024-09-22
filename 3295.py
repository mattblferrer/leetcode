class Solution:
    def reportSpam(self, message: list[str], bannedWords: list[str]) -> bool:
        matches = 0
        banned_set = set(bannedWords)

        for word in message:
            if word in banned_set:
                matches += 1
            if matches == 2:
                return True

        return False