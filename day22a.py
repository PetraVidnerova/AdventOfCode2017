positions = dict()

CLEAN, WEAK, INFECT, FLAG = 0, 1, 2, 3 

size = None
with open('input22.txt') as f:
    for i, line in enumerate(f):
        if i == 0: size = len(line.strip())
        for j, ch in enumerate(line):
            if ch == "#":
                positions[(i, j)] = INFECT
                

start = ( size // 2, size // 2)
UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3 
steps = {
    UP: (-1, 0),
    DOWN: (1, 0),
    LEFT: (0, -1),
    RIGHT: (0, 1)
}
direction = UP
count = 0 


def burst(pos, direction):
    global count
    global positions
    
    # change direction
    state = positions.get(pos, CLEAN)
    if state == CLEAN:
        direction = (direction - 1) % 4
    elif state == INFECT:
        direction = (direction + 1) % 4
    elif state == FLAG:
        direction = (direction + 2) % 4

    # infect node
    positions[pos] = (state + 1) % 4
    if positions[pos] == INFECT:
        count += 1

    #change position
    newpos = pos[0] + steps[direction][0], pos[1] + steps[direction][1]
    return newpos, direction

for _ in range(10000000):
    if _ % 1000 == 0:
        print(_)
    start, direction = burst(start, direction)
#    print("Infected: ", infected)
#    print("Weakened: ", weakened)
#    print("Flagged: ", flagged)
#    print()
    
print(count)

