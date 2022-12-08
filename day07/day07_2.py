import fileinput

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

smallest_size = float("inf")

for path, size in sizes.items():
    if size >= sizes["/"] - 40000000:
        smallest_size = min(smallest_size, size) 

print(smallest_size)
