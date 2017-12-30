programs = set()
beeing_hold = set()

with open('input07.txt') as f:
    for line in f:
        # add the program name to the list of all programs
        name = line.split()[0]
        programs.add(name)

        # add programs it is holding to list beeing_hold
        if '->' in line:
            names = line.split('->')[1]
            names = names.strip().split(', ')
            beeing_hold = beeing_hold | set(names)

print(programs - beeing_hold)


