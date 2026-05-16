nums = [2,7,11,15]
target = 26

def twoSum(nums, target):
    hash = {}
    for i , num in enumerate(nums):
        result = target - num
        if result in hash:
            return [hash[result],i]
        else:
            hash[num] = i

print(twoSum(nums,target))