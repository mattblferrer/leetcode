class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        contains_ball = [] # indices of boxes that contains one ball
        for i, box in enumerate(boxes):
            if box == '1':
                contains_ball.append(i)

        answer = []
        for i in range(len(boxes)):
            min_steps = 0
            for box in contains_ball:  # steps = distance from ball to box
                min_steps += abs(box - i)

            answer.append(min_steps)

        return answer