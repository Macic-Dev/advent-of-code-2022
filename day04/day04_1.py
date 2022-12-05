import fileinput

counter = 0

for line in fileinput.input():
    line = line.strip()
    if line:
        first, second = line.split(",")
        first = set(range(int(first.split("-")[0]), int(first.split("-")[1]) + 1))
        second = set(range(int(second.split("-")[0]), int(second.split("-")[1]) + 1))
        if first.issubset(second) or first.issuperset(second):
            counter += 1

print(counter)
