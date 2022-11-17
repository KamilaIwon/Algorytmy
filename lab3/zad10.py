
def balanced_parentheses(n: int) -> str:
    if n == 0:
        return 1
    return balanced_parentheses(n-1) * ((4*n - 2)/(n+1))

print(balanced_parentheses(6))