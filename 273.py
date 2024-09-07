class Solution:
    def numberToWords(self, num: int) -> str:
        def groupToWords(num: int) -> str:
            num_words = {  # 1 - 9
                0: "",
                1: "One", 
                2: "Two", 
                3: "Three", 
                4: "Four", 
                5: "Five", 
                6: "Six", 
                7: "Seven", 
                8: "Eight", 
                9: "Nine"
            }
            ten_words = {   # 10 - 19
                10: "Ten",
                11: "Eleven",
                12: "Twelve", 
                13: "Thirteen", 
                14: "Fourteen",
                15: "Fifteen", 
                16: "Sixteen", 
                17: "Seventeen", 
                18: "Eighteen", 
                19: "Nineteen"
            }
            mult_ten_words = {  # multiples of 10 (20 - 90)
                2: "Twenty",
                3: "Thirty",
                4: "Forty",
                5: "Fifty", 
                6: "Sixty", 
                7: "Seventy", 
                8: "Eighty", 
                9: "Ninety"
            }

            group_repr = ""
            while num > 0:
                if num > 99:  # in the hundreds
                    hundreds, num = divmod(num, 100)
                    group_repr += num_words[hundreds] + " Hundred"
                if num > 19:
                    tens, num = divmod(num, 10)
                    group_repr += " " + mult_ten_words[tens]
                elif num > 9:
                    group_repr += " " + ten_words[num]
                    break
                group_repr += " " + str(num_words[num])
                break

            return group_repr.strip()  # strip any leading whitespace

        if num == 0:  # zero edge case
            return "Zero"

        group_words = {  # for groups of 3 digits
            1: "Thousand", 
            2: "Million", 
            3: "Billion"
        }
        num_arr = []  # split into 3 digit groups

        while num != 0:
            num_arr.append(num % 1000)  # from smallest to largest group
            num //= 1000

        english = ""
        for i, group in enumerate(num_arr):  # billions, millions, etc. 
            if group == 0:  # no need to print if group = 0 (eg. 1,000,000)
                continue
            if i:  # if there is a word for the group (billions, millions, ...)
                english = (groupToWords(group) + " " + group_words[i] + " " + 
                    english)
            else:
                english = groupToWords(group)

        return english.strip()  # strip whitespace