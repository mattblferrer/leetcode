class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        if letters[0] > target or letters[-1] <= target:
            return letters[0]

        left, right = 0, len(letters) - 1
        while left != right:
            guess = (left + right) // 2
            if letters[guess] > target:
                right = guess
            else:
                left = guess + 1
            
        return letters[left]