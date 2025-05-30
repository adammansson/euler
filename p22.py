def name_score(name):
    return sum([ord(c) - ord("A") + 1 for c in name[1:-1]])
with open("names.txt", "r") as f:
    print(sum([(i+1) * name_score(name) for i, name in enumerate(sorted(f.read().split(",")))]))

