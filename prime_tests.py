
def prime_test_1(n): # Обычный тест на простоту
    for k in range (2, int(n / 2) + 1):
        if n % k == 0:
            return False
        return True
print(prime_test_1(17))

def prime_test_2(n): # Не совсем обычный тест на простоту
    if n % 2 == 0:
        return n == 2
    a = 3
    while a**2 <= n and n % a != 0:
        a += 2
    return a**2 > n
%timeit prime_test_1
print("1")
%timeit prime_test_2
print("2")
