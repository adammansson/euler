for k in range(1, 100):
    for m in range(2, 100, 2):
        a = k * (m**2 - 1)
        b = k * (2 * m)
        c = k * (m**2 + 1)
        if a + b + c == 1000:
            print(a * b * c)
            exit()
