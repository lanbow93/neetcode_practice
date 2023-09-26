# Solution attempt after watching javascript video before python video
# Results: Runtime 483ms - Beat 38.62% | Memory 30.78 - Beat 88.56%
def containsDuplicate(nums):
    return len(set(nums)) != len(nums)

# Solution attempt after watching video
# Results: Runtime 477ms - Beat 54.54% | Memory 31.78 - Beat 38.45%
def postContainsDuplicate(nums):
    numsHashset = set()
    for n in nums:
        if n in numsHashset:
            return True
        numsHashset.add(n)
    return False


