def findMissingRanges(nums, lower, upper):
    missing_ranges = []

    
    def addRange(start, end):
        if start == end:
            missing_ranges.append(str(start))
        else:
            missing_ranges.append(str(start) + '->' + str(end))

    
    if lower < nums[0]:
        addRange(lower, nums[0] - 1)


    for i in range(len(nums) - 1):
        if nums[i+1] - nums[i] > 1:
            addRange(nums[i] + 1, nums[i+1] - 1)

    
    if upper > nums[-1]:
        addRange(nums[-1] + 1, upper)

    return missing_ranges

# Driver code
nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99
result = findMissingRanges(nums, lower, upper)
print(result)  
