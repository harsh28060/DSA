# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]

def getConcatenation(nums):
    temp = nums
    return nums + temp
nums = [1,2,1]
print(getConcatenation(nums))