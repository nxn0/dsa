class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D": 500,
            "M": 1000,
            "IV":4,
            "IX":9,
            "XL":40,
            "XC":90,
            "CD":400,
            "CM":900, 
            }
        
        a = ow = 0
        while ow <len(s):
            if ow<len(s)-1 and s[ow:ow+2] in values:
                a += values[s[ow:ow+2]]
                ow+=2
            else:
                a += values[s[ow]]
                ow+=1
        return a

      