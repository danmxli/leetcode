"""
naive recursion intuition:
there are two ways to get to step n:
 - from (n-1) by taking 1 step
 - from (n-2) by taking 2 steps
add the total number of combinations to get to (n-1) with the total number of combinations to get to (n-2)
"""
def climbStairs_naive(n: int) -> int:
    def num_of_steps(n: int) -> int:

        # base case
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # recursive sum
        return num_of_steps(n-1) + num_of_steps(n-2)

    return num_of_steps(n)


# using memoization
def climbStairs(n: int) -> int:
    # memo hashtable with base cases
    memo = {1:1, 2:2}

    def num_of_steps(n: int) -> int:

        # function at specific value already computed
        if n in memo:
            return memo[n]

        # base case
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # store function at specific value
        memo[n] = num_of_steps(n-1) + num_of_steps(n-2)
        return memo[n]
    
    return num_of_steps(n)
