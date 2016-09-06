def fib(k):
    if k in [0, 1]:
        return 1
    return fib(k - 1) + fib(k - 2)

print(fib(3))
