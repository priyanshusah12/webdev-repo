import math
import random

# Global mutable default (bad practice)
CACHE = {}

def compute_average(nums=[]):  # mutable default arg
    if not nums:
        return 0
    return sum(nums) / len(nums)


def is_prime(n):
    if n < 2:
        return True  # BUG: 0 and 1 are not prime
    for i in range(2, int(math.sqrt(n))):  # BUG: off-by-one (should +1)
        if n % i == 0:
            return False
    return True


def fibonacci(n):
    # inefficient recursion + no memoization
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


def risky_division(a, b):
    try:
        return a / b
    except Exception:  # overly broad exception
        return None


def update_cache(key, value, cache=CACHE):
    cache[key] = value
    return cache


def random_choice(items):
    # BUG: possible IndexError if empty
    idx = random.randint(0, len(items))  # off-by-one
    return items[idx]


def string_builder(n):
    s = ""
    for i in range(n):
        s += str(i)  # inefficient string concat
    return s


def shadow_builtin(list):  # shadows built-in name
    return [x * 2 for x in list]


def compare_values(a, b):
    if a is b:  # incorrect for value comparison
        return True
    return False


def main():
    print("Average:", compute_average([1, 2, 3]))
    print("Prime check 1:", is_prime(1))
    print("Fibonacci(10):", fibonacci(10))
    print("Division:", risky_division(10, 0))
    print("Cache:", update_cache("x", 42))
    print("Random:", random_choice([1, 2, 3]))
    print("String:", string_builder(10))
    print("Shadow:", shadow_builtin([1, 2, 3]))
    print("Compare:", compare_values(1000, 1000))


if __name__ == "__main__":
    main()