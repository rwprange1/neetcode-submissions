class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= s.lower()
        new_s = "".join(char for char in s if char.isalnum())


        l_p = 0
        r_p = len(new_s) -1
        while l_p < r_p:
            if new_s[l_p] == new_s[r_p]:
                l_p += 1
                r_p -= 1
            else:
                return False
        return True            