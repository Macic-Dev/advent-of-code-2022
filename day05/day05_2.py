import fileinput

stacks = []

for line in fileinput.input():
    if line.strip():
        if line.startswith("move"):
            move = [int(x) for x in line.split() if x.isdigit()]
            crates = stacks[move[1]-1][:move[0]]
            for crate in crates:
                stacks[move[1]-1].remove(crate)
            crates.extend(stacks[move[2]-1])
            stacks[move[2]-1] = crates
        else:
            for i in range(1, len(line), 4):
                try:
                    stacks[(i-1)//4]
                except IndexError:
                    stacks.append([])    
                if line[i].isupper():
                    stacks[(i-1)//4].append(line[i])

for stack in stacks:
    print(stack[0])

