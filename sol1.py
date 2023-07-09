def threeSumClosest(nums, target):
    nums.sort()
    n = len(nums)
    closest_sum = float('inf')

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum

            if current_sum > target:
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                return current_sum

    return closest_sum

# Driver code
nums = [-1, 2, 1, -4]
target = 1
result = threeSumClosest(nums, target)
print(result)  # Output: 2
