class Solution:
    def countAndSay(self, n: int) -> str:
        num = "1"
        
        for _ in range(n-1):
            rle = ""
            current_digit = num[0]
            counter = 0
            
            for i in range(len(num)):
                if num[i] == current_digit:
                    counter += 1  # count consecutive digits
                else:
                    rle += str(counter) + str(current_digit)
                    current_digit = num[i]
                    counter = 1  # reset counter (counting num[i], hence 1)

            rle += str(counter) + str(current_digit)
            num = rle

        return num
