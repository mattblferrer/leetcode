class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def finalEditString(s: str) -> str:
            edited = []
            for char in s:
                if char == "#":  # backspace
                    if edited:  # check if there is character to backspace
                        edited.pop()
                else:
                    edited.append(char)
            return "".join(edited)

        return finalEditString(s) == finalEditString(t)