# Solution attempt before watching video
# Results: Runtime 537ms - Beat 39.06% | Memory 16.98 MB - Beat 97.91%
def two_sums(nums, target):
    for i in range(len(nums)):
        if(target- nums[i]  != nums[i]):
            if (target - nums[i]) in nums:
                return [i, nums.index(target - nums[i] )]
        elif(target - nums[i] == nums[i] ):
            try:
                return [i, nums.index(target-nums[i] , i+1)]
            except ValueError:
                continue

# Solution attempt after watching video
# Results: Runtime 54ms - Beat 96.21% | Memory 17.65 MB - Beat 29.28%
def post_two_sums(nums, target):
    numDict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in numDict:
            return [i, numDict[complement]]
        numDict[num] = i

print(post_two_sums([2,7,11,15], 9))
print(post_two_sums([3,2,4, 6],6))