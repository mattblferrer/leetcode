class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        bill_count = [0] * 3  # 5, 10, 20

        for bill in bills:
            if bill == 5:
                bill_count[0] += 1  # take 5
            elif bill == 10:
                if not bill_count[0]:
                    return False

                bill_count[1] += 1  # take 10
                bill_count[0] -= 1  # give 5
            elif bill == 20:
                bill_count[2] += 1  # take 20

                # give change for 20
                if bill_count[0] and bill_count[1]:  # give 10 + 5
                    bill_count[0] -= 1
                    bill_count[1] -= 1

                elif bill_count[0] > 2:  # give 3 x 5
                    bill_count[0] -= 3

                else:  # giving change for 20 is impossible
                    return False
        
        return True