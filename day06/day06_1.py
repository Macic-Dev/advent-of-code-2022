import fileinput

for line in fileinput.input():
    line = line.strip()
    if line:
        for i in range(0, len(line)-3):
            if len({*line[i:i+4]}) == 4:
                print(i+4)
                break
