class Solution:
    def reverseString(self, s):
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1
        print(s)

obj = Solution()
s = ["h","e","l","l","o"]
print(len(s))
obj.reverseString(s)