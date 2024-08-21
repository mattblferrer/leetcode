class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        matches = 0

        for item in items:
            if ruleKey == "type" and ruleValue == item[0]:
                matches += 1
            elif ruleKey == "color" and ruleValue == item[1]:
                matches += 1
            elif ruleKey == "name" and ruleValue == item[2]:
                matches += 1

        return matches