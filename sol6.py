def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# Driver code
nums = [2, 2, 1]
result = singleNumber(nums)
print(result)  # Output: 1
