found = None
n = 1
for k in range(1, 100):
    for m in range(2, 100, 2):
        a = k * (m**2 - n**2)
        b = k * (2 * m * n)
        c = k * (m**2 + n**2)
        if a + b + c == 1000:
            print(a * b * c)
            exit()
