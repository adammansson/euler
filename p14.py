mr = 1000000
cls = [0 for _ in range(mr)]
cls[1] = 1
mcl = 1
mn = 1
for sn in range(2, mr):
    n = sn
    cl = 1
    while n != 1:
        if n < mr and cls[n] != 0:
            cl += cls[n]
            break
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        cl += 1
    cls[sn] = cl
    if cl > mcl:
        mcl = cl
        mn = sn
print(mn)

