import fileinput

sum = 0
counter = 0
group_rucksacks = []

for line in fileinput.input():
    line = line.strip()
    if counter < 3:
        if line:
            group_rucksacks.append(line)
        counter += 1
    else:
        common_type = set(group_rucksacks[0]).intersection(group_rucksacks[1], group_rucksacks[2]).pop()
        if common_type.isupper():
            sum += ord(common_type) - 38
        else:
            sum += ord(common_type) - 96
        group_rucksacks = [line]
        counter = 1

print(sum)
