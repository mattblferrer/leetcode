class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        pref_length = len(pref)
        pref_num = 0  # number of words that contain pref as a prefix
        for word in words:  
            if word[:pref_length] == pref:
                pref_num += 1
            
        return pref_num