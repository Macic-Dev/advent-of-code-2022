import fileinput

score = 0

for line in fileinput.input():
    if line.strip():
        opponent, me = line.strip().split(" ")
        if opponent == "A":
            if me == "X":
                score += 3
            elif me == "Y":
                score += 4
            else:
                score += 8
        elif opponent == "B":
            if me == "X":
                score += 1
            elif me == "Y":
                score += 5
            else:
                score += 9
        else:
            if me == "X":
                score += 2
            elif me == "Y":
                score += 6
            else:
                score += 7

print(score)
