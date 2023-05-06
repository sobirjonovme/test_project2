class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        there_is_break = False
        result = ""

        for i in s:
            if i == " ":
                there_is_break = True
                continue

            if there_is_break:
                result = i
                there_is_break = False
                continue

            result += i

        return len(result)
