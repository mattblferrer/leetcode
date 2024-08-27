class Solution:
    def minimumPushes(self, word: str) -> int:
        unique_letters = set()
        for letter in word:  # add unique letters to set (no duplicates)
            if letter not in unique_letters:
                unique_letters.add(letter)

        unique_num = len(unique_letters)
        pushes = 0
        for i in range(unique_num):
            pushes += i // 8 + 1  # 8 keys on keypad 

        return pushes