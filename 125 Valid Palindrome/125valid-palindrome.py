class Solution:
    def isPalindrome(self, s: str) -> bool:
        return(s:=re.sub('\W|_','',s.lower()))==s[::-1]