# lc 1553. Minimum Days to Eat N Oranges
def minDays(n: int) -> int:

    # memoization
    memo = {}

    def dp(n: int) -> int:
        if n < 2:
            return n

        if n in memo:
            return memo[n]

        # eat 2 oranges
        eat_two = 1 + (n % 2) + dp(n // 2)
        # eat 3 oranges
        eat_three = 1 + (n % 3) + dp(n // 3)

        # return the minimum of the two
        memo[n] = min(eat_two, eat_three)
        return memo[n]
    
    return dp(n)

print(minDays(10))