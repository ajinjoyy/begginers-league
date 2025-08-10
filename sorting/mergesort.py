def merge_sort_lists(left, right):
    i = j = 0
    merged = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1
    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged

def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge_sort_lists(left, right)

nums = [38, 27, 43, 3, 9, 82, 10]
print("Original:", nums)
sorted_nums = merge_sort(nums)
print("Sorted:", sorted_nums)
