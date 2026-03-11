def searchInSortedArray(nums,target):
    start, end = 0, len(nums) - 1
    while start<=end:
        mid = (start + end) // 2
        if target == nums[mid]:
            return mid
        if nums[start] <= nums[mid]:
            if nums[start] <= target and nums[mid] >= target:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if nums[mid] <= target and nums[end] >= target:
                start = mid + 1
            else:
                end = mid - 1
    return -1


nums = [4,5,6,7,0,1,2] 
target = 0
print(searchInSortedArray(nums,target))


