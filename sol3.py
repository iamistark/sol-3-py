def nextPermutation(nums):
    n = len(nums)
    partition_index = -1


    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i+1]:
            partition_index = i
            break

    if partition_index == -1:
    
        nums.reverse()
        return nums

    
    swap_index = -1
    for i in range(n - 1, partition_index, -1):
        if nums[i] > nums[partition_index]:
            swap_index = i
            break

    
    nums[partition_index], nums[swap_index] = nums[swap_index], nums[partition_index]

    
    left = partition_index + 1
    right = n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    return nums

# Driver code
nums = [1, 2, 3]
result = nextPermutation(nums)
print(result)  # Output: [1, 3, 2]
