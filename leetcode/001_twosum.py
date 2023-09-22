"""
Leetcode #1
Given a list of integers and a target integer,
find the two integers that sum to the target
and return their indices

Assume there is only one solution, and that
no repeat elements are allowed
"""


def twoSum(nums: [int], target: int):
        dicto = {}
        for i in range(len(nums)):
            dicto[nums[i]] = i
            
            # set key=#, val=idx
            # overwrites previous dict entries if there are repeats
            # which is ok bc the next time we iterate from the beginning again
            
        for i in range(len(nums)):
            to_target = target - nums[i]
            try:
                if dicto[to_target] != i:
                    return [i, dicto[to_target]]
            except:
                pass

def twoSumBetter(nums: [int], target: int):
    hash = {}
    for i in range(len(nums)):
        complement = target - nums[i]       # calculate whats needed to add w/ nums[i] to target
        try:
            if hash[complement] is not None:            # if it exists
                return [hash[complement], i]
        except:
            hash[nums[i]] = i

print(twoSumBetter([2,7,11,15],9))
#print(twoSum([2,5,5,11], 10))


