def remove_duplicates(nums):
    if not nums:
        return 0
    
    write_index = 1  
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[write_index] = nums[i]
            write_index += 1
    
    return write_index

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k = remove_duplicates(nums)
print("Output:", k)
print("Updated nums:", nums[:k] + ['_'] * (len(nums) - k))
