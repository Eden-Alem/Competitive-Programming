class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        
        def checkConsecutive(answerKey):
            operation = k

            left, right = 0, 0
            max_ans = 0

            while right < n:
                if answerKey[right] == "T":
                    pass
                elif operation > 0:
                    operation -= 1
                else:
                    while answerKey[left] == "T":
                        left += 1

                    left += 1

                max_ans = max(max_ans, right - left + 1)
                right += 1

            return max_ans
        
        reverse = "".join(["T" if x == "F" else "F" for x in answerKey])
        return max(checkConsecutive(answerKey), checkConsecutive(reverse))
        
        
        
        