# GG REVIEW LATER
class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        def dfs_visit(u):
            for x in range(k):
                e = u * 10 + x
                if e not in visited:
                    visited.add(e)
                    v = e % MOD
                    dfs_visit(v)
                    ans.append(str(x))

        # driver
        MOD = 10 ** (n - 1)
        visited = set()
        ans = []
        dfs_visit(0)
        ans.append("0" * (n - 1))
        return "".join(ans)