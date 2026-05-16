# Input: nums = [1,2,3,1]
nums = [1,2,3,4]

def containsDuplicate(nums):
        return len(nums) != len(set(nums))

print(containsDuplicate(nums))