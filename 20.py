class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            # opening brackets
            if char == "(":
                stack.append(")")
            elif char == "{":
                stack.append("}")
            elif char == "[":
                stack.append("]")

            # closing brackets
            elif char in ")}]":  
                # check stack to see if valid
                if not stack:  # if stack is empty, closing is invalid
                    return False
                if stack.pop(-1) != char:
                    return False

        # check if stack is empty
        if not stack:
            return True
        return False