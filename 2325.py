class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key_order = dict()
        current_key = 97  # ASCII 'a'

        for char in key:  # create key substitution table
            if char == ' ':  # spaces not counted in key
                continue
            if char not in key_order:
                key_order[char] = chr(current_key)
                current_key += 1
        
        decoded = ""
        for char in message:
            if char == ' ':  # spaces not encoded
                decoded += ' '
            else:
                decoded += key_order[char]
        return decoded