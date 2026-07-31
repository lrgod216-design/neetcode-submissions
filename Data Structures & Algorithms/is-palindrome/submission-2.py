class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_String = ""
        for c in s:
            if c.isalnum():
                new_String += c.lower()
        return new_String == new_String[::-1]