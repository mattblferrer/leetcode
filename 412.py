class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        answer = []
        for i in range(1, n+1):
            string = ""

            # check divisibility
            if i % 3 == 0:
                string += "Fizz"
            if i % 5 == 0:
                string += "Buzz"
            if string == "":  # if not divisible
                string = str(i)
            
            answer.append(string)

        return answer