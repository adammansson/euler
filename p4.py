for a in range(9, -1, -1):
    for b in range(9, -1, -1):
        for c in range(9, -1, -1):
            p = 1*a + 10*b + 100*c + 1000*c + 10000*b + 100000*a
            for i in range(999, 99, -1):
                iq, r = divmod(p, i)
                if iq > 1000:
                    continue
                if r == 0:
                    print(p)
                    exit()

