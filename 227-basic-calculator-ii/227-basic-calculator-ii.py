class Solution:
    def calculate(self, s: str) -> int:
        ans = 0
        prev = 0
        curr = 0
        op = '+'

        for i, c in enumerate(s):
            if c.isdigit():
                curr = curr * 10 + int(c)
            if not c.isdigit() and c != ' ' or i == len(s) - 1:
                if op == '+' or op == '-':
                    ans += prev
                    prev = (curr if op == '+' else -curr)
                elif op == '*':
                    prev *= curr
                elif op == '/':
                    prev = int(prev / curr)
                op = c
                curr = 0

        return prev + ans