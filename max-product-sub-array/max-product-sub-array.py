
def maxProduct(nums):
    res = max(nums)
    curr_max = curr_min = 1
    for n in nums:
        temp = curr_max * n
        curr_max = max(temp, curr_min * n, n)
        curr_min = min(temp, curr_min * n, n)

        res = max(res, curr_max)
    return res

nums = [2,3,-2,4]
print(maxProduct(nums))