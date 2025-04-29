"""
four approaches to DP 😭😭😭😭
1. naive recursion
2. memoization (top-down) 
3. tabulation (bottom-up)
4. constant space (use variables)
"""

"""
example: find the nth fibonacci number
f(0) = 0
f(1) = 1
f(n) = f(n-1) + f(n-2)
"""

# naive recursion 😭
# grind recursion problems (i.e. recursive backtracking) and study decision trees and the call stack until it starts clicking eventually
def fib_recursive(n: int) -> int:
    if n == 0 or n == 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

# top down memo intuition -> OPTIMIZE RECURSIVE SOLUTION AFTER U FIND IT!!!
# avoid calling the function at the same value more than once
def fib_memo(n: int) -> int:
    
    # maintain a dictionary (initially with base cases) to remember the results 
    f_memo = {0:0, 1:1}

    # recursive implementation
    def f(n: int) -> int:
        ...
        if n in f_memo:
            return f_memo[n]
        
        # store the return value of each function call at a unqiue value in f_memo
        f_memo[n] = f(n-1) + f(n-2)
        return f_memo[n]
    
    return f(n)


# tabulation (aka bottom-up) does not implement recursion -> INSTEAD CREATE A TABLE
# why is initial intuition always super hard 😭
def fib_tabulation(n: int) -> int:
    # the next number is always the sum of the previous 2 numbers
    # don't forget about the base case
    table = [0] * (n+1)
    table[1] = 1
    
    # loop starts after the base case
    for i in range(2, n+1):
        table[i] = table[i-1] + table[i+2]
    
    return table[n]