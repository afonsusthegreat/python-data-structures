class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            x = str(x)
            x = list(x)
            tmnh = len(x) // 2
            for i in range(tmnh):
                if x[i] != x[-(i + 1)]:
                    return False
            return True
