class Solution:
    def maxProduct(self, words):
        max_product = 0
        for i in range(0, len(words)):
            for j in range(i + 1, len(words)):
                if set(words[i]) & set(words[j]) == set():
                    max_product = max(len(words[i]) * len(words[j]), max_product)
        return max_product