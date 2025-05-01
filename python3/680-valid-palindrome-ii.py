class Solution:
    def validPalindrome(self, s: str) -> bool:

        def twoPointer(s: str) -> bool:
            left = 0
            right = len(s) - 1
            isDeleted = False
            while left <= right:
                if s[left] != s[right]:
                    if isDeleted:
                        return False
                    else:
                        isDeleted = True
                        right -= 1
                        continue

                left += 1
                right -= 1
            return True
                
        return twoPointer(s) or twoPointer(s[::-1])


sol = Solution()
print(sol.validPalindrome(s = "deeee"))