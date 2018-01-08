pipes = {}
all_programs = []

#read input
with open("input12.txt") as f:
    for line in f:
        left, right = line.split("<->")
        pipes[int(left)] = list(map(int, right.split(",")))
        all_programs.append(int(left))

        
def find_group(xx):
    expand = [ xx ]
    programs = { xx }

    while expand:
        to_expand = expand.pop()
        new_programs = pipes[to_expand]
        for x in new_programs:
            if x not in programs:
                programs.add(x)
                expand.append(x)

    return programs


groups = 0
while all_programs:
    head = all_programs.pop()
    groups += 1
    for x in find_group(head):
        if x != head:
            all_programs.remove(x)

print(groups)
