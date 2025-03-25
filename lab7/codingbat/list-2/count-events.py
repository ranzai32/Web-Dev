def count_evens(nums):
    count = 0
    for num in nums:
        if num % 2 == 0:
            count += 1
    return count

def big_diff(nums):
    return max(nums) - min(nums)

def centered_average(nums):
    nums_sorted = sorted(nums)
    trimmed = nums_sorted[1:-1] 
    return sum(trimmed) // len(trimmed)

def sum13(nums):
    total = 0
    i = 0
    while i < len(nums):
        if nums[i] == 13:
            i += 2  
        else:
            total += nums[i]
            i += 1
    return total

def sum67(nums):
    total = 0
    in_section = False
    for num in nums:
        if num == 6:
            in_section = True
        elif in_section:
            if num == 7:
                in_section = False
        else:
            total += num
    return total

def has22(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i + 1] == 2:
            return True
    return False
