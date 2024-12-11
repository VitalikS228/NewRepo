def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0: return False
    return True
def is_power_of_five(n):
    if n < 1: return False
    while n % 5 == 0: n //= 5
    return n == 1
