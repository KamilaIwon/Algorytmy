# silnia

def factorial(n: int):
    if n == 0:
        return 1
    return(n * factorial(n-1))

print(factorial(5))
    