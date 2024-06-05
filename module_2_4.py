numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
a = 0
for i in numbers[1:]:
    for j in range(2, i + 1):
        if i % j == 0:
            a += 1
    if a == 1:
        primes.append(i)
    else:
        not_primes.append(i)
    a = 0
print('Primes:', primes)
print('Not primes:', not_primes)
