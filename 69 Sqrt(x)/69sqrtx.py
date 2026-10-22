class Solution:
    def mySqrt(self, x: int) -> int:
        if x== 0:
            return 0
        squirt = x
        for _ in range (100):
            squirt = (squirt+x/squirt)/2
        return int(squirt)
       