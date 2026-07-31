class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        s_clean = s.replace(" ", "").lower()
        for c in s_clean:
            if c.isalnum():
                result += c
        i, j = 0, len(result) - 1

        while i < j:
            if result[i] != result[j]:
                return False
            i += 1
            j -= 1
        return True
        