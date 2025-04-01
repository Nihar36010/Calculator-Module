import math

def add(a, b):
    x = a + b
    return x

def subtract(a, b):
    x = a - b
    return x

def multiply(a, b):
    x = a * b
    return x

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    x = a / b
    return x

def power(a, b):
    x = a ** b
    return x

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of a negative number.")
    x = a ** 0.5
    return x

def factorial(n):   
    if n < 0:
        raise ValueError("Cannot take factorial of a negative number.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def logarithm(a, base):
    if a <= 0 or base <= 1:
        raise ValueError("Invalid input for logarithm.")
    x = math.log(a, base)
    return x

def remainder(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    x = a % b
    return x

def absolute_value(a):
    x = abs(a)
    return x

def sine(a):
    x = math.sin(a)
    return x

def cosine(a):
    x = math.cos(a)
    return x

def tangent(a):
    x = math.tan(a)
    return x

def factorial_recursive(n):
    if n < 0:
        raise ValueError("Cannot take factorial of a negative number.")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    if a == 0 or b == 0:
        raise ValueError("Cannot calculate LCM of zero.")
    return abs(a * b) // gcd(a, b)

def permutation(n, r):
    if n < 0 or r < 0 or n < r:
        raise ValueError("Invalid input for permutation.")
    return factorial(n) // factorial(n - r)

def combination(n, r):
    if n < 0 or r < 0 or n < r:
        raise ValueError("Invalid input for combination.")
    return factorial(n) // (factorial(r) * factorial(n - r))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    if n <= 0:
        raise ValueError("Fibonacci sequence is not defined for non-positive integers.")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

def prime_factors(n):
    if n <= 1:
        raise ValueError("Prime factors are not defined for numbers less than or equal to 1.")
    factors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors

def lcm_of_list(numbers):
    if not numbers:
        raise ValueError("List cannot be empty.")
    lcm_value = numbers[0]
    for num in numbers[1:]:
        lcm_value = lcm(lcm_value, num)
    return lcm_value

def hcf_of_list(numbers):
    if not numbers:
        raise ValueError("List cannot be empty.")
    hcf_value = numbers[0]
    for num in numbers[1:]:
        hcf_value = gcd(hcf_value, num)
    return hcf_value

def is_armstrong_number(num):
    if num < 0:
        raise ValueError("Armstrong number is not defined for negative integers.")
    num_str = str(num)
    num_length = len(num_str)
    sum_of_powers = sum(int(digit) ** num_length for digit in num_str)
    return sum_of_powers == num

def is_palindrome(num):
    if num < 0:
        raise ValueError("Palindrome is not defined for negative integers.")
    return str(num) == str(num)[::-1]

def is_perfect_number(num):
    if num < 1:
        raise ValueError("Perfect number is not defined for non-positive integers.")
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisors_sum == num

def is_abundant_number(num):
    if num < 1:
        raise ValueError("Abundant number is not defined for non-positive integers.")
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisors_sum > num

def is_deficient_number(num):
    if num < 1:
        raise ValueError("Deficient number is not defined for non-positive integers.")
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisors_sum < num

def is_square_number(num):
    if num < 0:
        raise ValueError("Square number is not defined for negative integers.")
    return math.isqrt(num) ** 2 == num

def is_cube_number(num):
    if num < 0:
        raise ValueError("Cube number is not defined for negative integers.")
    return round(num ** (1/3)) ** 3 == num

def is_triangular_number(num):
    if num < 0:
        raise ValueError("Triangular number is not defined for negative integers.")
    n = int((math.sqrt(8 * num + 1) - 1) / 2)
    return n * (n + 1) // 2 == num

def is_hexagonal_number(num):
    if num < 0:
        raise ValueError("Hexagonal number is not defined for negative integers.")
    n = (math.sqrt(8 * num + 1) + 1) / 4
    return n.is_integer()

def is_pentagonal_number(num):
    if num < 0:
        raise ValueError("Pentagonal number is not defined for negative integers.")
    n = (math.sqrt(24 * num + 1) + 1) / 6
    return n.is_integer()

def is_kaprekar_number(num):
    if num < 0:
        raise ValueError("Kaprekar number is not defined for negative integers.")
    square = str(num ** 2)
    d = len(str(num))
    left_part = int(square[:-d]) if square[:-d] else 0
    right_part = int(square[-d:])
    return left_part + right_part == num

def is_fibonacci_number(num):
    if num < 0:
        raise ValueError("Fibonacci number is not defined for negative integers.")
    a, b = 0, 1
    while a < num:
        a, b = b, a + b
    return a == num

def is_happy_number(num):
    if num < 1:
        raise ValueError("Happy number is not defined for non-positive integers.")
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(digit) ** 2 for digit in str(num))
    return num == 1

def is_neon_number(num):
    if num < 0:
        raise ValueError("Neon number is not defined for negative integers.")
    return sum(int(digit) for digit in str(num ** 2)) == num

def is_disarium_number(num):
    if num < 0:
        raise ValueError("Disarium number is not defined for negative integers.")
    num_str = str(num)
    return sum(int(digit) ** (i + 1) for i, digit in enumerate(num_str)) == num

def is_automorphic_number(num):
    if num < 0:
        raise ValueError("Automorphic number is not defined for negative integers.")
    square = str(num ** 2)
    return square.endswith(str(num))

def is_strong_number(num):
    if num < 0:
        raise ValueError("Strong number is not defined for negative integers.")
    return sum(factorial(int(digit)) for digit in str(num)) == num

def is_smith_number(num):
    if num < 0:
        raise ValueError("Smith number is not defined for negative integers.")
    if is_prime(num):
        return False
    sum_of_digits = sum(int(digit) for digit in str(num))
    sum_of_prime_factors = sum(int(digit) for digit in str(sum(prime_factors(num))))
    return sum_of_digits == sum_of_prime_factors

def is_palindromic_prime(num):
    if num < 0:
        raise ValueError("Palindromic prime is not defined for negative integers.")
    return is_prime(num) and str(num) == str(num)[::-1]

def is_emirp(num):
    if num < 0:
        raise ValueError("Emirp number is not defined for negative integers.")
    reversed_num = int(str(num)[::-1])
    return is_prime(num) and is_prime(reversed_num) and num != reversed_num

def is_lychrel_number(num):
    if num < 0:
        raise ValueError("Lychrel number is not defined for negative integers.")
    iterations = 0
    while iterations < 50:
        num += int(str(num)[::-1])
        if str(num) == str(num)[::-1]:
            return False
        iterations += 1
    return True

def is_sphenic_number(num):
    if num < 1:
        raise ValueError("Sphenic number is not defined for non-positive integers.")
    prime_factors_list = prime_factors(num)
    return len(prime_factors_list) == 3 and all(is_prime(factor) for factor in prime_factors_list)

def is_circular_prime(num):
    if num < 0:
        raise ValueError("Circular prime is not defined for negative integers.")
    num_str = str(num)
    for i in range(len(num_str)):
        if not is_prime(int(num_str[i:] + num_str[:i])):
            return False
    return True

def is_bouncy_number(num):
    if num < 0:
        raise ValueError("Bouncy number is not defined for negative integers.")
    increasing = decreasing = False
    prev_digit = num % 10
    num //= 10
    while num > 0:
        curr_digit = num % 10
        if curr_digit < prev_digit:
            increasing = True
        elif curr_digit > prev_digit:
            decreasing = True
        if increasing and decreasing:
            return True
        prev_digit = curr_digit
        num //= 10
    return False

def is_harshad_number(num):
    if num < 0:
        raise ValueError("Harshad number is not defined for negative integers.")
    return num % sum(int(digit) for digit in str(num)) == 0