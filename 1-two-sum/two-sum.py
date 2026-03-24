class Solution:
    def twoSum(self, nums, target):
        hashmap = {}  # число -> индекс

        for i, num in enumerate(nums):
            complement = target - num  # число, которое нужно найти

            # если уже есть такое число
            if complement in hashmap:
                return [hashmap[complement], i]

            # сохраняем текущее число
            hashmap[num] = i