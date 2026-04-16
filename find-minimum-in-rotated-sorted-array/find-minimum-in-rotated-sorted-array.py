def findMin(nums):
    start = 0
    end = len(nums) - 1

    while start < end:
        mid = (start + end) // 2
        print(start, end)
        print(mid)
        if nums[mid] < nums[end]:
            end = mid
        else:
            start = mid + 1

    return nums[start]

nums = [3,4,5,1,2]
print(findMin(nums))