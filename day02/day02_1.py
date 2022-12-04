import fileinput

score = 0

for line in fileinput.input():
    if line.strip():
        opponent, me = line.strip().split(" ")
        if opponent == "A":
            if me == "X":
                score += 4
            elif me == "Y":
                score += 8
            else:
                score += 3
        elif opponent == "B":
            if me == "X":
                score += 1
            elif me == "Y":
                score += 5
            else:
                score += 9
        else:
            if me == "X":
                score += 7
            elif me == "Y":
                score += 2
            else:
                score += 6

print(score)
