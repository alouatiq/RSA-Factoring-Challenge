#!/usr/bin/env python3

import sys
from math import sqrt

def factorize(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return i, n // i
    return n, 1

def main(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                num = int(line.strip())
                p, q = factorize(num)
                print(f"{num}={p}*{q}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except ValueError:
        print(f"Error: Invalid number in the file.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)
    main(sys.argv[1])
