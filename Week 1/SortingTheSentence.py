class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(" ")
        
        val = []
        for i in range(len(words)):
            mini = i
            for j in range(i+1, len(words)):
                if (words[mini][-1] > words[j][-1]):
                    mini = j
            words[i], words[mini] = words[mini], words[i]
            val.append(words[i][:-1])
        
        return " ".join(val)