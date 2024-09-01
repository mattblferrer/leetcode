class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes = dict()
        for i in range(lowLimit, highLimit + 1):
            ball_sum = sum(int(d) for d in str(i))  # sum of digits
            if ball_sum not in boxes:
                boxes[ball_sum] = 1
            else:
                boxes[ball_sum] += 1

        return max(boxes.values())