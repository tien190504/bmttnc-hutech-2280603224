from math import sqrt

def is_prime(n):
    if n <= 1: return False
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    for i in range(5, int(sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

number = int(input("Nhập vào số cần kiểm tra:"))

if is_prime(number):
    print(f"{number} là số nguyên tố")
else:
    print(f"{number} không là số nguyên tố")