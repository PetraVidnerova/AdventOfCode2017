pipes = {}

#read input
with open("input12.txt") as f:
    for line in f:
        left, right = line.split("<->")
        pipes[int(left)] = list(map(int, right.split(",")))


expand = [ 0 ]
programs = { 0 }

while expand:
    to_expand = expand.pop()
    new_programs = pipes[to_expand]
    for x in new_programs:
        if x not in programs:
            programs.add(x)
            expand.append(x)

print(len(programs))
