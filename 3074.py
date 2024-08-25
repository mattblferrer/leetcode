class Solution:
    def minimumBoxes(self, apple: list[int], capacity: list[int]) -> int:
        capacity.sort()
        boxes_used = 0
        total_apples = sum(apple)

        for box in reversed(capacity):
            total_apples -= box
            boxes_used += 1
            if total_apples <= 0:
                break

        return boxes_used