import fileinput

sum = 0
pwd = []
sizes = {}

for line in fileinput.input():
    line = line.strip()
    if line:
        words = line.split()
        if line.startswith("$ "):
            if words[1] == "cd":
                if words[2] == "..":
                    pwd.pop()
                else:
                    pwd.append(words[2])
        else:
            if words[0].isnumeric():
                size = int(words[0])
                for i in range(1, len(pwd)+1):
                    path = "/".join(pwd[:i])
                    try:
                        sizes[path]
                    except KeyError:
                        sizes[path] = 0
                    sizes[path] += size

for path, size in sizes.items():
    if size <= 100000:
        sum += size

print(sum)
