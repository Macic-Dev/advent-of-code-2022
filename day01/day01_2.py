import fileinput

counter = 0
calories = []

for line in fileinput.input():
    if line.strip():
        counter += int(line)
    else:
        calories.append(counter)
        counter = 0

calories.sort(reverse=True)
print(sum(calories[:3]))
