#!/usr/bin/env python3

import sys
import random
from math import gcd, sqrt, exp, log

def is_probable_prime(n, k=5):
    if n < 2: return False
    for p in [2,3,5,7,11,13,17,19,23,29]:
        if n % p == 0: return n == p
    s, d = 0, n-1
    while d % 2 == 0:
        s, d = s+1, d//2
    for i in range(k):
        x = pow(random.randint(2, n-1), d, n)
        if x == 1 or x == n-1: continue
        for r in range(s-1):
            x = pow(x, 2, n)
            if x == n-1: break
        else: return False
    return True

def quadratic_sieve(n):
    def f(x): return (x*x - n) % n
    
    m = int(exp(sqrt(log(n) * log(log(n)))) / 2)
    factor_base = [p for p in range(2, m) if is_probable_prime(p) and n % p != 0]
    
    x = int(sqrt(n))
    while True:
        y = f(x)
        if y == 0:
            return gcd(x-sqrt(n), n)
        smooth = y
        for p in factor_base:
            while smooth % p == 0:
                smooth //= p
        if smooth == 1 or smooth == -1:
            return gcd(y, n)
        x += 1

def main(filename):
    try:
        with open(filename, 'r') as file:
            n = int(file.readline().strip())
            p = quadratic_sieve(n)
            q = n // p
            print(f"{n}={p}*{q}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except ValueError:
        print(f"Error: Invalid number in the file.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: rsa <file>")
        sys.exit(1)
    main(sys.argv[1])
