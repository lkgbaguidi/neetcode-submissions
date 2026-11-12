class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isalphanum(s : str) -> bool:
            if 'a' <= s <= 'z' or 'A' <= s <= 'Z' or '0' <= s <= '9':
                return True
            return False
        l,r = 0, len(s) - 1
        while l < r:
            while not isalphanum(s[l]) and l < r:
                l+=1
            
            while not isalphanum(s[r]) and l < r:
                r-=1
            
            if s[l].lower() != s[r].lower():
                return False
            
            else:
                l+=1
                r-=1
        return True

        



        