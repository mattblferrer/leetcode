class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        pointer = 0  # pointer on target
        curr = 1
        operations = []

        while pointer < len(target):
            operations.append("Push")
            if target[pointer] == curr:  # to keep element, push
                pointer += 1
            else:  # to discard element, push then pop
                operations.append("Pop")
            curr += 1

        return operations