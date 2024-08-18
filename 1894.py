class Solution:
    def chalkReplacer(self, chalk: list[int], k: int) -> int:
        k = k % sum(chalk)  # replace k with equivalent after student loop
        
        # find student in student loop
        for student, c in enumerate(chalk):
            if k < c:  # if student needs to replace the chalk
                return student
            k -= c  # use chalk to solve the problem
            