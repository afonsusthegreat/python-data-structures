def isdupe(nums):
    seen = {}
    for i in nums:
        if i in seen:
            return i
        else:
            seen.add(i)
