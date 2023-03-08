class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        memo = {}
        MOD = ((10**9) + 7)
        def ways(sp, step):
            if step == 0:
                if sp == endPos:
                    return 1
                return 0

            if (sp, step) in memo:
                return memo[(sp, step)]

            memo[(sp, step)] = (ways(sp - 1, step - 1) + ways(sp + 1, step - 1)) % MOD

            return memo[(sp, step)]

        return ways(startPos, k)