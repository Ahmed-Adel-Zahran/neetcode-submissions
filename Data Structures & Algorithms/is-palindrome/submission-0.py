class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = True
        s = "".join(filter(str.isalnum, s))
        s = s.replace(" ", "") 
        s = s.upper()
        print(s)
        for i in range(len(s)):
            j = len(s) - 1 - i
            if s[i] != s[j]:
                print("s[i] = ", i )
                print("s[j]=" ,j)
                return False
        return res