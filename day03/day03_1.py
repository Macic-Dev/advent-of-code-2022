import fileinput

sum = 0

for line in fileinput.input():
    line = line.strip()
    if line:
        compartment_size = len(line) // 2
        first_compartment, second_compartment = line[:compartment_size], line[compartment_size:]
        common_type = set(first_compartment).intersection(second_compartment).pop()
        if common_type.isupper():
            sum += ord(common_type) - 38
        else:
            sum += ord(common_type) - 96

print(sum)
