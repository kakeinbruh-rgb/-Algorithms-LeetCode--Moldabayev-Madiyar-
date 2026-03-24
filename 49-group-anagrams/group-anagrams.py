class Solution:
    def groupAnagrams(self, strs):
        anagrams = {}  # ключ -> список слов

        for word in strs:
            # сортируем слово для получения ключа
            key = ''.join(sorted(word))

            if key not in anagrams:
                anagrams[key] = []

            anagrams[key].append(word)

        # возвращаем только группы
        return list(anagrams.values())