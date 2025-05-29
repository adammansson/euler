ps = [2, 3, 5, 7, 11, 13, 17, 19]
mm = {p: 0 for p in ps}
for n in range(2, 21):
    for p in ps:
        m = 0
        while n % p == 0:
            m += 1
            n /= p
        mm[p] = max(mm[p], m)
pr = 1
for p, m in mm.items():
    pr *= p ** m
print(pr)
