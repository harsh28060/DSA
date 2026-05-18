class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = "".join(char.lower() for char in s if char.isalnum())
        return result == result[::-1]