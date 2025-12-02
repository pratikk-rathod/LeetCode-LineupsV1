class Solution(object):
    def countTrapezoids(self, points):
        MOD = 10**9 + 7
        from collections import Counter
        
        ycount = Counter(y for _, y in points)

        combos = []
        for cnt in ycount.values():
            if cnt >= 2:
                combos.append(cnt * (cnt - 1) // 2)

        if len(combos) < 2:
            return 0

        total_sum = 0
        sum_squares = 0

        for c in combos:
            c_mod = c % MOD
            total_sum = (total_sum + c_mod) % MOD
            sum_squares = (sum_squares + (c_mod * c_mod) % MOD) % MOD

        result = (total_sum * total_sum - sum_squares) % MOD
        result = result * pow(2, MOD - 2, MOD)  

        return result % MOD
