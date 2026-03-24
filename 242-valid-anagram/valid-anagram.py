class Solution:
    def isAnagram(self, s, t):
        # если длины разные — не анаграммы
        if len(s) != len(t):
            return False

        count = {}

        # считаем частоты символов в первой строке
        for char in s:
            count[char] = count.get(char, 0) + 1

        # уменьшаем счётчики по второй строке
        for char in t:
            if char not in count:
                return False
            count[char] -= 1

            if count[char] == 0:
                del count[char]

        return len(count) == 0