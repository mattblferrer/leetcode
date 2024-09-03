class Solution:
    def sortVowels(self, s: str) -> str:
        vowel_freq = [0] * 10  # for A, E, I, O, U, a, e, i, o, u
        vowel_list = [letter for letter in 'AEIOUaeiou']
        vowel_set = set(vowel_list)  # for faster lookup

        for letter in s:  # find vowel frequencies in s
            if letter not in vowel_set:
                continue
            for i, search in enumerate(vowel_list):  
                if letter == search:  # if vowel, find ASCII position
                    vowel_freq[i] += 1
                    break
        
        t_list = []  # list of characters in t
        for letter in s:
            if letter not in vowel_set:  # consonant
                t_list.append(letter)
            else:  # vowel
                for i in range(10):
                    if vowel_freq[i]:
                        vowel_freq[i] -= 1
                        t_list.append(vowel_list[i])
                        break

        return "".join(t_list)