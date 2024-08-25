class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        def splitIntoWords(sentence: str) -> list[str]:
            return sentence.split(" ")

        index = 1
        final_sentence = ""
        words = splitIntoWords(sentence)
        for word in words:  # convert each word to Goat Latin
            if word[0] in 'aeiouAEIOU':  # starts with vowel
                new_word = word + "ma" + "a" * index
            else:  # starts with consonant
                new_word = word[1:] + word[0] + "ma" + "a" * index
            final_sentence += new_word + " "
            index += 1

        return final_sentence[:-1]  # remove trailing space