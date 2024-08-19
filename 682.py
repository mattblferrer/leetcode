class Solution:
    def calPoints(self, operations: list[str]) -> int:
        record = []
        for operation in operations:
            if operation == "+":  # record sum of previous 2 scores
                record.append(record[-1] + record[-2])

            elif operation == "D":  # record double of the previous score
                record.append(record[-1] * 2)

            elif operation == "C":  # invalidate previous score
                record.pop()

            else:  # integer x
                record.append(int(operation))
            
        return sum(record)  # total of scores