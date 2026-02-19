def ispalindrome(s):
    s = list(s)
    for index in range((len(s) // 2) + 1):
        if s[index] != s[-(index + 1)]:
            return False
    return True
