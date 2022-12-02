import fileinput

score = [0, 0]

for line in fileinput.input():
    if line.strip():
        opponent, me = line.strip().split(" ")
        if opponent == "A":
            if me == "X":
                score[0] += 4
                score[1] += 3
            elif me == "Y":
                score[0] += 8
                score[1] += 4
            else:
                score[0] += 3
                score[1] += 8
        elif opponent == "B":
            if me == "X":
                score[0] += 1
                score[1] += 1
            elif me == "Y":
                score[0] += 5
                score[1] += 5
            else:
                score[0] += 9
                score[1] += 9
        else:
            if me == "X":
                score[0] += 7
                score[1] += 2
            elif me == "Y":
                score[0] += 2
                score[1] += 6
            else:
                score[0] += 6
                score[1] += 7

print(score[0])
print(score[1])
