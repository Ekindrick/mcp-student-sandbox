def average_ratios(numbers):
    nums = [n for n in numbers if n != 0]
    if not nums:
        raise ValueError("no non-zero numbers")
    total = sum(100 / n for n in nums)
    return total / len(nums)

print(average_ratios([10, 5, 0]))
