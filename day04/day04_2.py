import fileinput

counter = 0

for line in fileinput.input():
    line = line.strip()
    if line:
        first, second = line.split(",")
        first = [int(x) for x in first.split("-")]
        second = [int(x) for x in second.split("-")]
        if not (first[1] < second[0] or first[0] > second[1]):
            counter += 1

print(counter)
