def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
n = 1
c = 1
while c < 10001:
    n += 2
    if is_prime(n):
        c += 1
print(n)

