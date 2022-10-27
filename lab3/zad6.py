
import math

def prime(n: int)-> bool:
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if prime(i):
            if n % i == 0:
                return False
    return True

print(prime(7))
print(prime(8))