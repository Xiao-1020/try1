def fibonacci_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]
n=int(input())
print("{:.2f}".format(fibonacci_memo(n)))