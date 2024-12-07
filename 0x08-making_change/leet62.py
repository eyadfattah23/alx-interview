def uniquePaths(m: int, n: int, memo=None) -> int:

    if not memo:
        memo = [[-1 for _ in range(n)] for __ in range(m)]
    if memo[m-1][n-1] != -1:
        return memo[m-1][n-1]

    if m == 0 or n == 0:
        return 0

    if m == 1 and n == 1:
        return 1

    memo[m-1][n-1] = uniquePaths(m, n-1, memo) + uniquePaths(m - 1, n, memo)

    return memo[m-1][n-1]


print(uniquePaths(3, 3))
