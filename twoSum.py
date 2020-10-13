# Naive / Brute Force Approach 

nums = [1,2,7,15]
target = 9
def twosum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            summation = nums[i] + nums[j]
            if summation == target:
                return [i, j]


print(twosum(nums, target))


# Optimize / Efficient Approach
nums = [2,7,11,15]
target = 9

def sumQuestion (nums, target):


    compainionMap = dict()

    for i in range(len(nums)):

        val = target - nums[i]
       
        if nums[i] in compainionMap:

            return [compainionMap[nums[i]],i]

        else:
            compainionMap[val] = i





print(sumQuestion(nums, target))
