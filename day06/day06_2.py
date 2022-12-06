import fileinput

for line in fileinput.input():
    line = line.strip()
    if line:
        for i in range(0, len(line)-13):
            if len({*line[i:i+14]}) == 14:
                print(i+14)
                break
