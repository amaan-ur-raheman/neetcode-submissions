class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        n = len(s)

        for i in range(n):
            char = set()

            for j in range(i, n):
                if s[j] in char:
                    break
                
                char.add(s[j])
                res = max(res, len(char))
            
        return res