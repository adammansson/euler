with open("p13.txt", "r") as f:
    print(sum([int(n) for n in f.readlines()]) // 10**42)

