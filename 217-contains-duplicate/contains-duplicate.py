class Solution:
    def containsDuplicate(self, nums):
        seen = set()  # множество для хранения уникальных значений

        for num in nums:
            if num in seen:
                return True  # найден дубликат
            seen.add(num)

        return False  # дубликатов нет