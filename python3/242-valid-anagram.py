from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        store = defaultdict(int)
        
        size1 = len(s)
        for c1 in s:
            store[c1] += 1
        
        size2 = len(t)
        for c2 in t:
            if not store[c2]:
                return False    
            else:
                store[c2] -= 1

        if size1 != size2:
            return False
        
        return True

sol = Solution()
print(sol.isAnagram("anagram", "nagaram"))