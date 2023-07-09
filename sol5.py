def plusOne(digits):
    n = len(digits)
    carry = 1

    for i in range(n - 1, -1, -1):
        digits[i] += carry
        if digits[i] > 9:
            digits[i] = digits[i] % 10
            carry = 1
        else:
            carry = 0

    if carry == 1:
        digits.insert(0, 1)

    return digits

# Driver code
digits = [1, 2, 3]
result = plusOne(digits)
print(result)  # Output: [1, 2, 4]
