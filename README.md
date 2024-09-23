# RSA Factoring Challenge

## Description
This project is part of the RSA Factoring Challenge, focusing on factorizing numbers used in RSA encryption. The goal is to factor these numbers as quickly as possible to decode encrypted documents.

## Project Structure
```
RSA-Factoring-Challenge/
├── factors
├── rsa
├── tests/
│   ├── test00
│   ├── rsa-1
│   ├── rsa-2
│   ├── rsa-15
│   └── rsa-16
└── README.md
```

## Files
- `factors`: Script to factorize numbers into a product of two smaller numbers
- `rsa`: Script to factorize RSA numbers into two prime factors
- `tests/`: Directory containing test files

## Requirements
- Language: Python 3
- OS: Standard Ubuntu 20.04 LTS

## Usage

### Task 0: Factorize all the things!
```bash
./factors <file>
```
Example:
```bash
./factors tests/test00
```

### Task 1: RSA Factoring Challenge
```bash
./rsa <file>
```
Example:
```bash
./rsa tests/rsa-1
```

## Performance Note
The current implementation may not be efficient enough for very large numbers within the 5-second time limit. For better performance, consider optimizing the algorithms or implementing them in a compiled language like C.

## Author
AL OUATIQ H.