class Solutions(object):
    def TwoSum(self, nums, target):
        num_to_index = {}
        for i, num in enumerate(nums):
            if (target - num) in nums:
                return [num_to_index[target-num], i ]
                num_to_index[num] = i
        return []