class DynamicProgramming:
    """
    Practice fundamental Dynamic Programming patterns (1D Memoization & Tabulation).
    """

    def climb_stairs(self, n: int) -> int:
        """
        You are climbing a staircase. It takes n steps to reach the top.
        Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
        
        Example:
            n = 2 -> 2 (1+1, 2)
            n = 3 -> 3 (1+1+1, 1+2, 2+1)
        """
        if n <= 2:
            return n
        prev2, prev1 = 1, 2
        for _ in range(3, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
        return prev1

    def coin_change(self, coins: list[int], amount: int) -> int:
        """
        You are given an integer array coins representing coins of different denominations 
        and an integer amount. Return the fewest number of coins that you need to make up that amount.
        If that amount cannot be made up, return -1.
        
        Example:
            coins = [1, 2, 5], amount = 11 -> 3 (5 + 5 + 1)
            coins = [2], amount = 3 -> -1
            coins = [1], amount = 0 -> 0
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], dp[a - c] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
